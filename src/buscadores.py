
## @brief Excepción personalizada para manejar errores en la definición de intervalos de fechas.
#  @details Se lanza cuando los valores de inicio y final de un intervalo no son coherentes
#  (p.ej., la fecha final es anterior a la fecha inicial) o tienen un formato
#  incorrecto.
class IntervaloException(Exception):

    ## @brief Constructor para la IntervaloException.
    #
    #  @param message El mensaje descriptivo del error.
    def __init__(self, message: str):
        raise Exception("\n--->IntervaloException::__init__. NO IMPLEMENTADO!!!\n")


from abc import ABC, abstractmethod



## @brief Interfaz para un componente de búsqueda (Strategy Pattern).
#  @details Define el contrato para cualquier clase que implemente una estrategia de búsqueda
#  sobre un conjunto de publicaciones. Se espera que la clase que implemente
#  esta interfaz almacene internamente los criterios de búsqueda específicos
#  (p.ej., un autor, palabras clave, etc.).
class Buscador(ABC):

    ## @brief Ejecuta una búsqueda sobre el mapa de publicaciones proporcionado,
    #  utilizando los criterios definidos en la implementación de la clase.
    #  NO LO MOFIFIQUÉIS
    #
    #  @param publicaciones El mapa completo de publicaciones (ID -> Publicacion)
    #  sobre el cual se realizará la búsqueda.
    #  @return Una Lista (List) de objetos Publicacion que coinciden con los
    #  criterios de búsqueda internos de la implementación.
    @abstractmethod
    def busca(self, publicaciones):
        pass



# Asumimos que 'Buscador' y 'Publicacion' están disponibles

## @brief Excepción personalizada para errores en el intervalo de fechas.
class IntervaloException(Exception):
    pass


## @brief Implementación de la interfaz Buscador que filtra publicaciones
#  basándose en un intervalo de fechas (inclusive).
#  @details Las fechas (inicio y fin) deben proporcionarse en formato String "AAAAMM".
class BuscadorPorIntervalo(Buscador):

    ## @brief Constructor para BuscadorPorIntervalo.
    #  Valida que las fechas tengan el formato correcto "AAAAMM" (6 caracteres)
    #  y que el intervalo sea coherente (fin >= inicio).
    #
    #  @param inicio El string de la fecha inicial (formato "AAAAMM").
    #  @param fin El string de la fecha fin (formato "AAAAMM").
    #  @throws IntervaloException Si las fechas no tienen 6 caracteres
    #  (AAAAMM) o si la fecha fin es anterior a la fecha inicial.
    def __init__(self,inicio,fin):
        raise Exception("\n--->BuscadorPorIntervalo::__init__. NO IMPLEMENTADO!!!\n")

    ## @brief Busca en el mapa de publicaciones y devuelve una lista de aquellas
    #  cuya fecha de publicación esté dentro del intervalo [inicio, fin].
    #  @details La comparación tiene en cuenta tanto el año como el mes mediante
    #  orden lexicográfico de cadenas.
    #
    #  @param publicaciones El mapa completo de publicaciones
    #  (ID -> Publicacion) sobre el cual se realizará la búsqueda.
    #  @return Una Lista de objetos Publicacion cuya fecha ("AAAAMM")
    #  esté dentro del intervalo.
    def busca(self,publicaciones):
        raise Exception("\n--->BuscadorPorIntervalo::busca. NO IMPLEMENTADO!!!\n")

    # --- Getters ---

    ## @brief Obtiene la fecha de inicio del intervalo.
    #  @return La fecha "AAAAMM".
    def get_inicio(self):
        raise Exception("\n--->BuscadorPorIntervalo::get_inicio. NO IMPLEMENTADO!!!\n")

    ## @brief Obtiene la fecha fin del intervalo.
    #  @return La fecha "AAAAMM".
    def get_final(self):
        raise Exception("\n--->BuscadorPorIntervalo::get_final. NO IMPLEMENTADO!!!\n")



# Asumimos que Buscador, Publicacion y Autor están disponibles.

## @brief Implementación de la interfaz Buscador que filtra publicaciones
#  basándose en una lista de nombres de autores.
class BuscadorPorNombres(Buscador):

    ## @brief Constructor de BuscaPorNombres.
    #  Inicializa la lista interna de nombres de autores como una lista vacía.
    def __init__(self):
        raise Exception("\n--->BuscadorPorNombres::__init__. NO IMPLEMENTADO!!!\n")

    ## @brief Añade un nombre de autor a la lista de criterios de búsqueda.
    #
    #  @param nombre El nombre completo del autor a añadir. Debe seguir el
    #  formato "Nombre Apellidos" (nombre y apellidos separados
    #  por un espacio en blanco).
    def add_nombre(self,nombre: str):
        raise Exception("\n--->BuscadorPorNombres::add_nombre. NO IMPLEMENTADO!!!\n")

    ## @brief Busca en el mapa de publicaciones y devuelve una lista de aquellas
    #  que tengan al menos un autor que coincida con la lista interna.
    #  @details La comparación se realiza construyendo el nombre completo del autor
    #  de la publicación (concatenando su nombre y apellidos separados por
    #  un espacio en blanco) y comparándolo (ignorando mayúsculas/minúsculas)
    #  con los nombres de la lista interna.
    #
    #  La búsqueda interna se detiene (para esa publicación) tan pronto
    #  como se encuentra la primera coincidencia.
    #
    #  @param publicaciones El mapa completo de publicaciones
    #  (ID -> Publicacion) sobre el cual se realizará la búsqueda.
    #  @return Una Lista de objetos Publicacion que coinciden con los
    #  criterios (autores) definidos.
    def busca(self,publicaciones):
        raise Exception("\n--->BuscadorPorNombres::__init__. NO IMPLEMENTADO!!!\n")

    # --- Getters ---

    ## @brief Obtiene la lista de nombres de autores utilizada para la búsqueda.
    #  @return La lista de nombres (formato "Nombre Apellidos").
    def get_nombres(self):
        raise Exception("\n--->BuscadorPorNombres::get_nombres. NO IMPLEMENTADO!!!\n")


# Asumimos que Buscador y Publicacion están disponibles.

## @brief Implementación de la interfaz Buscador que filtra publicaciones
#  basándose en una lista de palabras clave.
#  @details La búsqueda requiere que la publicación contenga TODAS las palabras clave
#  definidas en esta instancia de buscador EN MINÚSCULAS.
class BuscadorPorPalabrasClave(Buscador):

    ## @brief Constructor para BuscadorPorPalabrasClave.
    #  Inicializa la lista de palabras clave como una lista vacía.
    def __init__(self):
        raise Exception("\n--->BuscadorPorPalabrasClave::__init__. NO IMPLEMENTADO!!!\n")

    ## @brief Añade una palabra clave a la lista de búsqueda.
    #  La palabra se convierte a minúsculas antes de ser añadida.
    #
    #  @param palabra La palabra clave a añadir.
    def add_palabra(self,palabra):
        raise Exception("\n--->BuscadorPorPalabrasClave::add_palabra. NO IMPLEMENTADO!!!\n")

    ## @brief Busca en el mapa de publicaciones y devuelve una lista de aquellas
    #  cuyas palabras clave contengan *todas* las palabras clave definidas
    #  en el atributo palabras la lista de esta clase.
    #  @details La comparación ignora mayúsculas y minúsculas (asume que las palabras
    #  en la lista interna ya están en minúsculas).
    #
    #  @param publicaciones El mapa completo de publicaciones
    #  (ID -> Publicacion) sobre el cual se realizará la búsqueda.
    #  @return Una Lista de objetos Publicacion que cumplen
    #  con todos los criterios de palabras clave.
    def busca(self,publicaciones):
        raise Exception("\n--->BuscadorPorPalabrasClave::__init__. NO IMPLEMENTADO!!!\n")

    # --- Getters ---

    ## @brief Obtiene la lista de palabras clave de búsqueda.
    #  @return La lista de palabras clave (en minúsculas).
    def get_palabras(self):
        raise Exception("\n--->BuscadorPorPalabrasClave::get_palabras. NO IMPLEMENTADO!!!\n")

    def estan_todas(self,pub_keywords_lower):
        raise Exception("\n--->BuscadorPorPalabrasClave::estan_todas. NO IMPLEMENTADO!!!\n")
