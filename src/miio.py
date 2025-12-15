import sys
from dominio import *

# Asumimos que Autor, Publicacion, Libro y ArticuloEnRevista están disponibles.

## @brief Clase de utilidad para leer (parsear) un archivo de texto
#  y cargar los datos de publicaciones en un mapa.
class LectorPublicaciones:
    # Delimitadores definidos en el formato
    # Nota: En Python split() usa literales por defecto, no regex,
    # por lo que no hace falta escapar el pipe (|) a menos que usemos el módulo re.
    _DELIM_CAMPO = ";"
    _DELIM_LISTA = "|"
    _DELIM_AUTOR = ":"

    ## @brief Lee un archivo de texto estructurado y lo convierte en un mapa de
    #  objetos Publicacion.
    #  @details Toda la información de una única publicación debe estar en una sola línea.
    #  Los datos de la publicación estarán separados por delimitadores.
    #
    #  A continuación se listan dichos delimitadores:
    #  - **Delimitador de Campo Principal (atributo):** `;` (Punto y coma)
    #  - **Delimitador de Listas (para autores o palabras clave):** `|` (Barra vertical)
    #  - **Delimitador de nombre, apellido de Autor:** `:` (Dos puntos)
    #
    #  ### Formato de Línea LIBRO
    #
    #      TIPO;ID;TITULO;FECHA_AAAAMM;AUTORES;PALABRAS_CLAVE;EDITORIAL
    #
    #  Donde TIPO es "LIBRO".
    #
    #  - **Ejemplo AUTORES:** `"Robert C.:Martin:N/A|Erich:Gamma:N/A"`
    #  - **Ejemplo PALABRAS_CLAVE:** `"design|patterns|gof|oop"`
    #
    #  Ejemplo de línea para Libro:
    #      "LIBRO;LIB-003;Design Patterns...;199410;Erich:Gamma:N/A|...;design|patterns;Addison-Wesley"
    #
    #  @param nombre_archivo El path (ruta) y nombre del archivo a leer.
    #  @return Un diccionario (Dict[str, Publicacion]) donde la clave es el ID de la
    #  publicación.
    @staticmethod
    def leer(nombre_archivo):
        dic = {}
        file =  open(nombre_archivo, "r")
        for i in file.readlines():
            autor_lista = []  # objectes de classe autor
            print(i)
            temp = i.split("_DELIM_CAMPO") # temp es una llista
            autores = temp[4].split("_DELIM_LISTA") # llista de autors separada per | nom:cognom:cognom
            for k in autores:
                autor = Autor(k[0],k[1]) #nom i primer cognom
                autor_lista.append(autor)
            pub  = Publicacion(temp[2],temp[1],autor_lista,temp[3])#titulo, id, autores, palabras_clave, fecha
            dic[temp[1]] = pub


        return dic

