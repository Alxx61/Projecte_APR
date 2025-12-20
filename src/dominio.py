## @package bibliografia
#  @brief Módulo para la gestión de referencias bibliográficas.
#  @details Contiene las clases necesarias para gestionar autores, libros y artículos
#  usando el estilo de comentarios especiales de Doxygen.
from typing import Any


# Usamos 'Publicacion' como string para el type hinting (Forward declaration)
# asumiendo que la clase estará disponible en tiempo de ejecución.

## @brief Clase que representa a un autor.
#  @details Gestiona la información personal del autor y mantiene un registro
#  de sus publicaciones mediante un diccionario.
class Autor:
    ## @brief Contador estático para generar IDs únicos automáticamente.
    #  Equivalente a private static int idSiguienteAutor en Java.
    _id_siguiente_autor = 1

    ## @brief Constructor único que gestiona tanto el caso por defecto como el parametrizado.
    #  @details Asigna un ID único automáticamente e inicializa el diccionario de publicaciones.
    #  Si no se pasan argumentos, se inicializa con cadenas vacías (comportamiento del
    #  constructor por defecto de Java).
    #
    #  @param nombre El nombre del autor (opcional, por defecto "").
    #  @param apellidos Los apellidos del autor (opcional, por defecto "").
    #  @param institucion La institución del autor (opcional, por defecto "").
    def __init__(self,nombre: str = "",apellidos: str = "",institucion: str = ""):
        self.ID=self._id_siguiente_autor
        Autor._id_siguiente_autor+=1
        self.nombre=nombre
        self.apellidos=apellidos
        self.institucion=institucion
        self.publicaciones={}

    ## @brief Obtiene el ID único del autor.
    #  @return El ID del autor (entero).
    def get_id(self):
        return self.ID

    ## @brief Obtiene el nombre del autor.
    #  @return El nombre del autor.
    def get_nombre(self) :
        return self.nombre

    ## @brief Obtiene los apellidos del autor.
    #  @return Los apellidos del autor.
    def get_apellidos(self):
        return self.apellidos

    ## @brief Obtiene la institución del autor.
    #  @return La institución del autor.
    def get_institucion(self):
        return self.institucion

    ## @brief Obtiene el mapa de publicaciones del autor.
    #  @return Un diccionario (equivalente a HashMap) de las publicaciones.
    def get_publicaciones(self) :
        return self.publicaciones

    ## @brief Obtiene el contador estático para el siguiente ID de autor.
    #  @return El siguiente ID a utilizar.
    @staticmethod
    def get_id_siguiente_autor():
        return Autor._id_siguiente_autor

    ## @brief Añade una publicación al mapa de publicaciones de este autor.
    #  @details La clave utilizada será el ID de la publicación.
    #
    #  @param publicacion El objeto Publicacion a añadir.
    def add_publicacion(self,publicacion: 'Publicacion'):
        self.publicaciones[publicacion.get_ID()]=publicacion

    ## @brief Devuelve un String con la información del autor.
    #  @details NO MODIFICAR EL métode.
    #  @return String formateado como se indica en el documento enunciado del proyecto
    def __str__(self):
        result = f"{self.nombre}:{self.apellidos}"
        if not self.institucion:
            result +=":N/A"
        else:
            result +=f":{self.institucion}"
        return result

## @brief Clase abstracta que define una publicación genérica.
#  @details Define los atributos comunes y la estructura base para
#  libros y artículos.
class Publicacion:

    ## @brief Constructor parametrizado de Publicacion.
    #
    #  @param titulo El título de la publicación.
    #  @param id El identificador único de la publicación.
    #  @param autores La lista de autores (objetos de la clase Autor).
    #  @param palabras_clave Una lista de palabras clave.
    #  @param fecha La fecha de publicación (formato "AAAAMM").
    def __init__(self, titulo, id, autores, palabras_clave, fecha):
        self.titulo=titulo
        self.id=id
        self.autores=autores
        self.palabras_clave=palabras_clave
        self.fecha=fecha

    ## @brief Obtiene el título de la publicación.
    #  @return El título.
    def get_titulo(self):
        return self.titulo

    ## @brief Obtiene el ID de la publicación.
    #  @return El ID.
    def get_id(self):
        return self.id
        #raise Exception("\n--->Publicacion::get_id. NO IMPLEMENTADO!!!\n")

    ## @brief Obtiene las palabras clave de la publicación.
    #  @return Una lista de String con las palabras clave.
    def get_palabras_clave(self):
        return self.palabras_clave
        #raise Exception("\n--->Publicacion::get_palabras_clave. NO IMPLEMENTADO!!!\n")

    ## @brief Obtiene la lista de autores de la publicación.
    #  @return Una lista de objetos Autor.
    def get_autores(self) :
        return self.autores
        #raise Exception("\n--->Publicacion::get_autores. NO IMPLEMENTADO!!!\n")

    ## @brief Obtiene la fecha de publicación (formato "AAAAMM").
    #  @return La fecha (AAAAMM).
    def get_fecha(self):
        return self.fecha
        #raise Exception("\n--->Publicacion::get_fecha. NO IMPLEMENTADO!!!\n")

    ## @brief Genera la representación en String de los atributos comunes de
    #  todos los tipos de publicación.
    #  @details NO MODIFICAR EL métode.
    #  @return String formateado como se indica en el documento enunciado del proyecto
    def __str__(self):
        # 1. Formatear la lista de Autores
        # Se verifica si la lista existe y tiene contenido.
        # Se usa comprension de lista para convertir cada objeto Autor a string.
        txt_autores = ""
        if self.autores:
            txt_autores = "|".join([str(autor) for autor in self.autores])

        # 2. Formatear la lista de Palabras Clave
        txt_palabras = ""
        if self.palabras_clave:
            txt_palabras = "|".join(self.palabras_clave)

        # 3. Construcción final
        # Se mantiene la etiqueta "palabrasClave" en el string para coincidir con Java,
        # aunque la variable interna sea pythonica (_palabras_clave).
        return (f"id={self.id}; titulo={self.titulo}; fecha={self.fecha}; "
                f"autores=[{txt_autores}]; palabrasClave=[{txt_palabras}]")

# Asumimos que Publicacion y Autor están importados o disponibles en el namespace

## @brief Representa un libro, que es un tipo específico de publicación.
#  @details Extiende la clase Publicacion añadiendo el atributo de editorial.
class Libro(Publicacion):

    ## @brief Constructor parametrizado de Libro.
    #
    #  @param titulo El título del libro.
    #  @param id El identificador del libro.
    #  @param autores Lista de objetos Autor.
    #  @param palabras_clave lista de palabras clave (strings).
    #  @param fecha Año y mes de publicación.
    #  @param editorial La editorial del libro.
    def __init__(self, titulo, id, autores, palabras_clave, fecha, editorial):
        super().__init__(titulo, id, autores, palabras_clave, fecha)
        self.editorial=editorial
        #raise Exception("\n--->Libro::__init__. NO IMPLEMENTADO!!!\n")

    ## @brief Obtiene la editorial del libro.
    #  @return La editorial.
    def get_editorial(self):
        return self.editorial
        #raise Exception("\n--->Libro::get_editorial. NO IMPLEMENTADO!!!\n")

    ## @brief Devuelve una representación en String completa del Libro.
    #  @details NO MODIFICAR EL métode.
    #  @return String formateado como se indica en el documento enunciado del proyecto
    def __str__(self):
        return f"Libro;{super().__str__()}; editorial={self.editorial}"



## @brief Representa un artículo científico publicado en una revista.
#  @details Extiende la clase Publicacion añadiendo información específica
#  como el factor de impacto y el nombre de la revista.
class ArticuloEnRevista(Publicacion):

    ## @brief Constructor parametrizado de ArticuloEnRevista.
    #
    #  @param titulo El título del artículo.
    #  @param id El identificador del artículo.
    #  @param autores Lista de objetos Autor.
    #  @param palabras_clave lista de palabras clave.
    #  @param fecha Año y mes de publicación.
    #  @param factor_impacto El factor de impacto de la revista (float).
    #  @param revista El nombre de la revista.
    def __init__(self,titulo,id,autores,palabras_clave,fecha,factor_impacto,revista):
        super().__init__(titulo, id, autores, palabras_clave, fecha)
        self.factor_impacto=factor_impacto
        self.revista=revista



    ## @brief Obtiene el factor de impacto de la revista.
    #  @return El factor de impacto.
    def get_factor_impacto(self):
        return self.factor_impacto
        #raise Exception("\n--->ArticuloEnRevista::get_factor_impacto. NO IMPLEMENTADO!!!\n")

    ## @brief Obtiene el nombre de la revista.
    #  @return El nombre de la revista.
    def get_revista(self):
        return self.revista
        #raise Exception("\n--->ArticuloEnRevista::get_revista. NO IMPLEMENTADO!!!\n")

    ## @brief Devuelve una representación en String completa del Artículo.
    #  @details NO MODIFICAR EL métode.
    #  @return String formateado como se indica en el documento enunciado del proyecto
    def __str__(self):
        # Utilizamos super().__str__() para traer la cadena de la clase padre
        # y f-strings para formatear el resto exactamente como en Java.
        return (f"ArticuloEnRevista;{super().__str__()}, "
                f"factorImpacto={self.factor_impacto}; revista={self.revista}")
