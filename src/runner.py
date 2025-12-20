from caosdeuso import Controlador
from gestordatos import GestorDeDatos
from caosdeuso import Controlador
from comparadores import *
from buscadores import *
from ordenador import Ordenador



# Asumimos que todas las clases anteriores (Controlador, GestorDeDatos,
# Ordenador, Comparadores, Buscadores, Exceptions) están importadas.

## @brief Clase que ejecuta un escenario de prueba predefinido en memoria.
class EjecutorDesdeMemoria:

    ## @brief Constructor.
    #  @details Crea el atributo resultado como una lista vacía.
    def __init__(self):
        self.resultado=[]


    ## @brief Obtiene la lista de resultados acumulados.
    #  @return Lista de strings con el toString() de las publicaciones encontradas.
    def get_resultado(self):
        return self.resultado
        #raise Exception("\n--->EjecutorDesdeMemoria::__init__. NO IMPLEMENTADO!!!\n")

    ## @brief Ejecuta el escenario de prueba completo de búsqueda y ordenación.
    #
    #  @details El proceso detallado es el siguiente:
    #  1. Creará un objeto Controlador.
    #  2. Obtendrá las publicaciones invocando al métode
    #     GestorDeDatos.cargar_publicaciones_de_prueba().
    #  3. Añadirá estas publicaciones al Controlador.
    #
    #  4. Realizará una búsqueda de publicaciones por el nombre "Geoffrey Hinton".
    #
    #  5. Generará una lista con las publicaciones encontradas ordenadas por
    #     fecha en sentido ascendente.
    #  6. Para cada publicación de la lista generará un String invocando al
    #     métode __str__() y lo añadirá al atributo resultado.
    #  7. Generará una lista con las publicaciones encontradas ordenadas por
    #     fecha en sentido descendente.
    #  8. Para cada publicación de la lista generará un String y lo añadirá al resultado.
    #  9. Generará una lista con las publicaciones encontradas ordenadas por
    #     autor en sentido ascendente.
    #  10. Para cada publicación de la lista generará un String y lo añadirá al resultado.
    #  11. Generará una lista con las publicaciones encontradas ordenadas por
    #     autor en sentido descendente.
    #  12. Para cada publicación de la lista generará un String y lo añadirá al resultado.
    #
    #  13. Realizará una búsqueda de publicaciones por las siguientes palabras
    #     clave: "neural networks" y "optimization" (una sola búsqueda: se buscan
    #     publicaciones que contengan ambos valores).
    #  14. Repetirá los pasos 5 a 12 para la lista de publicaciones obtenidas.
    #
    #  15. Realizará una búsqueda de publicaciones cuya fecha de publicación
    #     esté dentro del intervalo "197001" y "198012".
    #  16. Repetirá los pasos 5 a 12 para la lista de publicaciones obtenidas.
    #
    #  @note PODÉIS DEFINIROS AQUEL(LOS) métode(S) ADICIONAL(ES) QUE
    #  CONSIDERÉIS OPORTUNO PARA ORGANIZAR EL CÓDIGO DE ESTA CLASE.

    def ejecuta(self):
        controlador = Controlador()
        datos = GestorDeDatos.cargar_publicaciones_de_prueba()
        for pub in datos.values():
            controlador.add_publicacion(pub)

        # 4
        buscador_nombres = BuscadorPorNombres()
        buscador_nombres.add_nombre("Geoffrey Hinton")
        controlador.set_buscador(buscador_nombres)

        # 5-12
        self._ejecutar_ciclo_ordenacion(controlador)

        # 13-14
        buscador_tags = BuscadorPorPalabrasClave()
        buscador_tags.add_palabra("neural networks")
        buscador_tags.add_palabra("optimization")
        controlador.set_buscador(buscador_tags)
        self._ejecutar_ciclo_ordenacion(controlador)

        # 15-16
        buscador_fecha = BuscadorPorIntervalo("197001", "198012")
        controlador.set_buscador(buscador_fecha)
        self._ejecutar_ciclo_ordenacion(controlador)

    def _ejecutar_ciclo_ordenacion(self, controlador):
        #Pasos 5-12
        configs = [
            (ComparadorFechas(), False),
            (ComparadorFechas(), True),
            (ComparadorApellidos(), False),
            (ComparadorApellidos(), True)
        ]

        for comp, desc in configs:
            ordenador = Ordenador(desc, comp)
            lista = controlador.buscar_y_ordenar(ordenador)
            for p in lista:
                self.resultado.append(str(p))




        """publicaciones=GestorDeDatos.cargar_publicaciones_de_prueba()
        controlador=Controlador()
        for i in publicaciones:
            self.add_publicacion=controlador.add_publicacion(i)

        self.resultado.append("--- Publicaciones cargadas inicialmente ---")
        self.resultado.extend([str(p) for p in self.publicacion])

        self.resultado.append("BUSQUEDA 1: Autor 'Geoffrey Hinton'")

        publicacion_h=self.buscar_por_autor("Geoffrey Hinton")
        self._repetir_ordenaciones(publicacion_h)

        self.resultados.append("BUSQUEDA 2:Palabras clave 'neural networks' y 'optimization'")
        palabras_clave=["neural networks", "optimization"]
        publicacion_keywords=self.buscar_por_palabras_clave(palabras_clave)
        self._repetir_ordenaciones(publicacion_keywords)

        self.resultado.append("BUSQUEDA 3:Intervalo de fecha '197001' a '198012'")
        publicacion_fecha=self.buscar_por_fecha("197001","198012")
        self._repetir_ordenaciones(publicacion_fecha)

        return self.resultado"""





