## @brief Controlador principal de la aplicación.
#  @details Gestiona las colecciones de autores y publicaciones, y
#  coordina las operaciones de búsqueda y ordenación.
class Controlador:

    ## @brief Constructor de Controlador.
    #  Inicializa los mapas (contenedores) de autores y publicaciones como
    #  colecciones vacías. Deja su atributo buscador a None.
    #  @note Muy importante: antes de invocar al métode buscar_y_ordenar,
    #  el atributo buscador debe referenciar a un objeto válido.
    def __init__(self):
        self.autores={}
        self.publicaciones={}
        self.buscador=None

    ## @brief Añade un autor al mapa de autores del controlador.
    #  Utiliza el ID del autor como clave.
    #
    #  @param autor El objeto Autor a añadir.
    def add_autor(self,autor):
        self.autores[autor.id]=autor


    ## @brief Añade una publicación al mapa de publicaciones.
    #  @details Este métode comprueba la lista de autores de la publicación.
    #  Si alguno de los autores (identificado por su ID) no existe
    #  en el mapa de autores del controlador, se añade a dicho mapa automáticamente.
    #
    #  @param publicacion La publicación a añadir.
    def add_publicacion(self, publicacion):
        for autor in publicacion.autors:
            if autor not in self.autores:
                self.autores[autor.id]=autor
        if publicacion.id not in self.publicaciones:
            self.publicaciones[publicacion.id]=publicacion


    ## @brief Ejecuta una búsqueda y ordena los resultados.
    #  @details Es necesario que el atributo buscador referencie a un objeto válido.
    #  El métode utiliza su atributo buscador para filtrar las publicaciones y
    #  luego utiliza el objeto ordenador proporcionado para ordenar esa lista.
    #
    #  @param ordenador El objeto (estrategia) Ordenador que se
    #  utilizará para ordenar los resultados de la búsqueda.
    #  @return Una <b>nueva</b> lista de Publicacion, filtrada y ordenada.
    def buscar_y_ordenar(self,ordenador):
        lista=self.buscador.filtrar(self.buscador)
        lista_ordenada=ordenador.ordenar(lista)
        return lista_ordenada

    # --- Getters y Setters ---

    ## @brief Obtiene el mapa de autores.
    #  @return El diccionario de autores.
    def get_autores(self):
        return self.autores


    ## @brief Obtiene el mapa de publicaciones.
    #  @return El diccionario de publicaciones.
    def get_publicaciones(self):
        return self.publicaciones

    ## @brief Obtiene el buscador (estrategia) asignado a este controlador.
    #  @return El objeto Buscador o None si no se ha asignado.
    def get_buscador(self):
        return self.buscador

    ## @brief Establece el buscador (estrategia) para este controlador.
    #  @param buscador El objeto Buscador.
    def set_buscador(self,buscador):
        self.buscador=buscador
