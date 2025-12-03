import os
import sys
import re
import math
from runner import EjecutorDesdeMemoria
from miio import *
from gestordatos import *



# Asumimos que todas las clases del sistema están disponibles e importadas.
# from ejecutor_desde_memoria import EjecutorDesdeMemoria
# from lector_publicaciones import LectorPublicaciones
# from gestor_de_datos import GestorDeDatos
# from publicacion import Publicacion

## @brief Clase encargada de corregir la ejecución del programa y asignar una nota.
#  @details Compara la salida generada por EjecutorDesdeMemoria con un fichero de
#  referencia y valida la lectura de archivos.
class CorrectorDeEjecutor:
    # Regex para parsear una línea de salida de toString()
    # Captura clave=valor, donde valor puede ser algo entre corchetes [...] o algo hasta la siguiente coma
    _CAMPO_PATTERN = re.compile(r"(\w+)=((?:\[.*?\])|(?:[^,]+))")

    # Tolerancia para el redondeo especial (10 elevado a -5).
    _TOLERANCIA = 1e-5

    ## @brief Clase interna (estructura) para almacenar el resultado de una comparación de línea.
    class _ResultadoComparacion:
        def __init__(self):
            self.score = 0.0
            self.max_score = 1.0  # Max. posible para la línea
            self.mismatches = []

    ## @brief Constructor. Inicializa notas a 0.
    def __init__(self):
        self._nota = 0.0
        ## @brief El resultado acumulado de la comparación de lectura de fichero.
        self._resultado_lectura_fichero = 0.0

    ## @brief Punto de entrada principal para la corrección de la gestión en memoria.
    def corrige_gestion_en_memoria(self):

        ejecutor = EjecutorDesdeMemoria()
        ejecutor.ejecuta()
        resultado_obtenido = ejecutor.get_resultado()

        lineas_referencia = []

        # Construir path al archivo de referencia
        path_referencia = os.path.join(os.getcwd(),"referencia_resultados.txt")

        try:
            with open(path_referencia,'r',encoding='utf-8') as f:
                # Leemos, normalizamos y filtramos
                for linea in f:
                    l_norm = CorrectorDeEjecutor._normalizar_linea(linea)
                    if l_norm.startswith("Libro;") or l_norm.startswith("ArticuloEnRevista;"):
                        lineas_referencia.append(l_norm)

        except FileNotFoundError:
            print("Error fatal: No se pudo leer 'referencia_resultados.txt'",file=sys.stderr)
            return
        except Exception as e:
            print(f"Error leyendo referencia: {e}",file=sys.stderr)
            return

        self._nota = self.corrige_resultado(resultado_obtenido,lineas_referencia)

        print("-------------------------------------------")
        print(f"NOTA DE EJECUTORDESDEMEMORIA: {self._nota:.2f} de 10.0")
        print("-------------------------------------------\n\n")

    ## @brief Devuelve la nota de gestión en memoria.
    #  @return Nota (float).
    def get_nota_gestion_en_memoria(self) -> float:
        return self._nota

    ## @brief Normaliza una línea eliminando espacios extra.
    @staticmethod
    def _normalizar_linea(linea) -> str:
        if linea is None:
            return ""
        # Reemplaza cualquier secuencia de espacios en blanco por un solo espacio
        return re.sub(r"\s+"," ",linea.strip())

    ## @brief Compara los dos listas de strings (obtenido y referencia) y calcula una nota.
    #  @param obtenido Lista de strings generada por el alumno.
    #  @param referencia Lista de strings esperada.
    #  @return La nota calculada sobre 10.
    def corrige_resultado(self,obtenido,referencia) :

        lineas_obtenidas = self._elimina_no_informacion(obtenido,"ArticuloEnRevista","Libro")
        lineas_referencia = self._elimina_no_informacion(referencia,"ArticuloEnRevista","Libro")

        num_obt = len(lineas_obtenidas)
        num_ref = len(lineas_referencia)

        # Lógica para determinar sobre cuál iterar (aunque en el bucle while se controla por índices)
        # En Java se usaban variables 'aIterar', 'laOtra' que luego no se usaban explícitamente
        # dentro del bucle while, ya que se usaban 'ref' y 'obt' por índice. Mantenemos lógica while.

        if not lineas_referencia:
            print("Error: El archivo de referencia no contiene líneas de publicación válidas.",file=sys.stderr)
            return 0.0

        puntuacion_total = 0.0
        lineas_corregidas = 0

        index_ref = 0
        index_obt = 0

        # Inicialización segura
        if num_ref > 0:
            ref = lineas_referencia[0]
        else:
            ref = ""

        if num_obt > 0:
            obt = lineas_obtenidas[0]
        else:
            obt = ""

        fin = (num_obt == 0 or num_ref == 0)

        while not fin:
            if index_obt == num_obt - 1 or index_ref == num_ref - 1:
                fin = True

            lineas_corregidas += 1

            # Calcula la puntuación Y los fallos
            resultado = CorrectorDeEjecutor._calcular_puntuacion_linea(obt,ref)

            # Evitar división por cero si no hay líneas obtenidas
            if num_obt > 0:
                puntuacion_total += resultado.score / num_obt

            # ---- MODIFICACIÓN: Imprimir error si no es perfecto ----
            if resultado.score < resultado.max_score:
                print(f"\n--- ERROR en Línea con información: {lineas_corregidas} ---")
                print("\tGenerada:")
                print(f"\t\t{obt}")
                print("\tReferencia:")
                print(f"\t\t{ref}")
                print(f"\t\tPartes no coincidentes: {resultado.mismatches}")
            else:
                # Mostramos acumulado proyectado sobre 10
                acumulado_imprimir = self._redondear(puntuacion_total * 10)
                print(f"OK en línea con información número: {lineas_corregidas}")
                print(f"\t Acumulado (sobre 10): {acumulado_imprimir}")

            if not fin:
                index_ref += 1
                index_obt += 1
                ref = lineas_referencia[index_ref]
                obt = lineas_obtenidas[index_obt]

        # Media Aritmética: (Suma de puntuaciones / Total de líneas) * 10
        return puntuacion_total * 10.0

    ## @brief Calcula la puntuación (0 a 1.0) para una sola línea y devuelve mismatches.
    @staticmethod
    def _calcular_puntuacion_linea(obt: str,ref: str) -> '_ResultadoComparacion':
        res = CorrectorDeEjecutor._ResultadoComparacion()

        tipo_ref_es_libro = ref.startswith("Libro[")
        tipo_obt_es_libro = obt.startswith("Libro[")

        if tipo_ref_es_libro != tipo_obt_es_libro:
            res.mismatches.append("TIPO_PUBLICACION")
            res.max_score = 1.0
            return res

        try:
            datos_ref = CorrectorDeEjecutor._parsear_linea_to_string(ref)
            datos_obt = CorrectorDeEjecutor._parsear_linea_to_string(obt)

            # Función auxiliar interna para chequear campos y sumar puntos
            def check_campo(clave,puntos,es_coleccion=False):
                val_ref = datos_ref.get(clave)
                val_obt = datos_obt.get(clave)

                match = False
                if es_coleccion:
                    match = CorrectorDeEjecutor._comparar_coleccion(val_ref,val_obt)
                else:
                    match = (val_ref == val_obt)

                if match:
                    res.score += puntos
                else:
                    res.mismatches.append(clave)

            res.max_score = 1.0

            if tipo_ref_es_libro:
                # --- Puntuación LIBRO ---
                check_campo("id",0.1)
                check_campo("titulo",0.1)
                check_campo("palabrasClave",0.35,es_coleccion=True)
                check_campo("fecha",0.1)
                check_campo("autores",0.25,es_coleccion=True)
                check_campo("editorial",0.1)
            else:
                # --- Puntuación ARTICULO ---
                check_campo("id",0.1)
                check_campo("titulo",0.1)
                check_campo("palabrasClave",0.3,es_coleccion=True)
                check_campo("fecha",0.1)
                check_campo("autores",0.2,es_coleccion=True)
                check_campo("factorImpacto",0.1)
                check_campo("revista",0.1)

        except Exception as e:
            res.score = 0.0
            res.mismatches.append(f"ERROR_PARSEO_LINEA (excepción: {type(e).__name__})")

        return res

    @staticmethod
    def _parsear_linea_to_string(linea):
        datos = {}
        # Extraer contenido entre el primer '[' y el último ']'
        start = linea.find('[') + 1
        end = linea.rfind(']')
        if start <= 0 or end <= 0:
            return datos

        contenido = linea[start:end]

        # Buscar todas las coincidencias de "clave=valor"
        for m in CorrectorDeEjecutor._CAMPO_PATTERN.finditer(contenido):
            datos[m.group(1)] = m.group(2)

        return datos

    @staticmethod
    def _comparar_coleccion(s1,s2) -> bool:
        if s1 is None or s2 is None:
            return s1 == s2

        # Eliminar corchetes iniciales y finales [ ... ]
        if len(s1) > 1: s1 = s1[1:-1]
        if len(s2) > 1: s2 = s2[1:-1]

        # Crear sets. Si la cadena está vacía, el set debe estar vacío.
        # split(", ") dividiría una cadena vacía en [''], creando un set con un elemento vacío.
        if not s1:
            set1 = []
        else:
            set1 = s1.split(", ")

        if not s2:
            set2 =[]
        else:
            set2 = s2.split(", ")

        return set1 == set2

    def _elimina_no_informacion(self,lista,uno: str,otro: str):
        resultado = []
        for s in lista:
            # Se usa strip() para asegurar que no fallen espacios
            if s.strip().startswith(uno) or s.strip().startswith(otro):
                resultado.append(s)
        return resultado

    def _redondear(self,valor: float) -> float:
        # Comprobamos el caso especial
        siguiente_entero = math.ceil(valor)
        diferencia = siguiente_entero - valor

        if 0 < diferencia < self._TOLERANCIA:
            return siguiente_entero

        # Redondeo estándar a 3 cifras decimales
        return round(valor * 1000.0) / 1000.0

    def _normalizar_string(self,s) -> str:
        if s is None:
            return ""
        return re.sub(r"\s+"," ",s.strip())

    def _redondear_para_imprimir(self,valor: float) -> float:
        # Misma lógica que _redondear
        return self._redondear(valor)

    ## @brief Compara los dos mapas de publicaciones.
    def _compara_mapas(self,mapa_fichero,
                       mapa_memoria):

        self._resultado_lectura_fichero = 0.0

        # Determinar mapa menor
        if len(mapa_fichero) < len(mapa_memoria):
            mapa_menor = mapa_fichero
        else:
            mapa_menor = mapa_memoria

        print(f"Iniciando comparación. Iterando sobre {len(mapa_menor)} claves.")

        # Calcular el incremento
        tam_max = max(len(mapa_fichero),len(mapa_memoria))
        if tam_max == 0:
            incremento = 0.0
        else:
            incremento = 10.0 / float(tam_max)

        for clave,pub_menor in mapa_menor.items():
            # Recuperar ambas publicaciones (buscamos en ambos mapas)
            pub_fichero = mapa_fichero.get(clave)
            pub_memoria = mapa_memoria.get(clave)

            if not pub_fichero or not pub_memoria:
                print(f"Aviso: La clave {clave} no existe en ambos mapas. Saltando.")
                continue

            # Comparar str() normalizados
            s_fichero = self._normalizar_string(str(pub_fichero))
            s_memoria = self._normalizar_string(str(pub_memoria))

            if s_fichero == s_memoria:
                self._resultado_lectura_fichero += incremento
                valor_imprimir = self._redondear_para_imprimir(self._resultado_lectura_fichero)
                print(f"Coincidencia en clave: {clave}. Resultado acumulado: {valor_imprimir}")
            else:
                print(f"--- FALLO en clave: {clave} ---")
                print(f"\tFichero: {s_fichero}")
                print(f"\tMemoria: {s_memoria}")

        print("Comparación finalizada.")

    ## @brief Devuelve el resultado final acumulado de lectura.
    def get_nota_lectura_fichero(self) -> float:
        return self._resultado_lectura_fichero

    ## @brief Método principal de ejecución para corrección de ficheros.
    def corrige_lectura_archivo(self):

        path_archivo = os.path.join(os.getcwd(),"publicaciones.txt")
        print(f"Leyendo desde fichero: {path_archivo}")

        mapa_fichero = LectorPublicaciones.leer(path_archivo)
        print(f"Publicaciones leídas de fichero: {len(mapa_fichero)}")

        print("Cargando desde GestorDeDatos...")
        mapa_memoria = GestorDeDatos.cargar_publicaciones_de_prueba()
        print(f"Publicaciones cargadas de memoria: {len(mapa_memoria)}")

        self._compara_mapas(mapa_fichero,mapa_memoria)



corrector = CorrectorDeEjecutor()

#1. Corrección en memoria
corrector.corrige_gestion_en_memoria()
nota_gestion = corrector.get_nota_gestion_en_memoria()

# 2. Corrección lectura fichero
corrector.corrige_lectura_archivo()
nota_fichero = corrector.get_nota_lectura_fichero()


# 3. Resultados finales
# Helper para formateo
def fmt(v): return str(corrector._redondear_para_imprimir(v))


# print("-------------------------------------------")
# print(f"NOTA DE CORRECCIÓN DE GESTIÓN EN MEMORIA: {fmt(nota_gestion)} de 10.0\n")
# print("-------------------------------------------\n\n")

print("-------------------------------------------")
print(f"NOTA DE CORRECCIÓN DE LECTURA DE ARCHIVO: {fmt(nota_fichero)} de 10.0\n")
print("-------------------------------------------\n\n")

nota_proyecto = (nota_gestion * 0.9) + (0.1 * nota_fichero)

print("-------------------------------------------")
print("NOTA DE PROYECTO \n\t0,9*NOTA DE CORRECCIÓN DE GESTIÓN EN MEMORIA + "
      "\n\t0,1*NOTA DE CORRECCIÓN DE LECTURA DE ARCHIVO.\n\tNOTA DE PROYECTO: "
      + fmt(nota_proyecto))
print("-------------------------------------------\n\n")