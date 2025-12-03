from typing import List


# Asumimos que Comparator y Publicacion están disponibles.

## @brief Clase que ordena una lista de objetos Publicacion utilizando
#  una estrategia de comparación (Comparator) y el algoritmo de la burbuja.
#  @details Esta clase NO modifica la lista original que recibe, sino que devuelve
#  una nueva lista con los elementos ordenados.
class Ordenador:

    ## @brief Constructor de la clase Ordenador.
    #
    #  @param descendente True si la ordenación debe ser en sentido descendente
    #  (mayor a menor), False si debe ser en sentido ascendente (menor a mayor).
    #  @param comparador El Comparator (p.ej., ComparadorAutores, ComparadorFecha)
    #  que se utilizará para ordenar la lista.
    def __init__(self,descendente,comparador):
        raise Exception("\n--->Ordenador::__init__. NO IMPLEMENTADO!!!\n")

    ## @brief Ordena la lista de publicaciones proporcionada utilizando el algoritmo
    #  de la burbuja (Bubble Sort).
    #  @details El método utiliza el comparador definido en el atributo de la
    #  clase y respeta el sentido (ascendente/descendente) del atributo descendente.
    #
    #  Este método NO modifica la lista original pasada como argumento.
    #
    #  @param publicaciones La lista de objetos Publicacion a ordenar.
    #  @return Una <b>nueva</b> lista que contiene las publicaciones ordenadas.
    def ordena(self,publicaciones):
        raise Exception("\n--->Ordenador::ordena. NO IMPLEMENTADO!!!\n")

    # --- Getters y Setters ---

    ## @brief Asigna el comparador.
    #  @param comparador El nuevo comparador a utilizar.
    def set_comparador(self,comparador):
        raise Exception("\n--->Ordenador::set_comparador. NO IMPLEMENTADO!!!\n")

    ## @brief Devuelve el valor de descendente.
    #  @return True si es descendente, False si es ascendente.
    def is_descendente(self):
        raise Exception("\n--->Ordenador::is_descendente. NO IMPLEMENTADO!!!\n")

    ## @brief Asigna valor a descendente.
    #  @param descendente Nuevo valor de descendente.
    def set_descendente(self,descendente):
        raise Exception("\n--->Ordenador::set_descendente. NO IMPLEMENTADO!!!\n")

    ## @brief Obtiene el comparador actual.
    #  @return El Comparator usado para ordenar.
    def get_comparador(self):
        raise Exception("\n--->Ordenador::get_comparador. NO IMPLEMENTADO!!!\n")
