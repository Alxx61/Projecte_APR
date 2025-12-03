from dominio import *
import os

## @brief Clase de utilidad (seeder) para generar  datos de prueba
#  con publicaciones reales (libros y artículos) para poblar la aplicación.
#  NO LO MODIFIQUÉIS
#  @details Contiene métodos estáticos para instanciar objetos y devolverlos
#  en estructuras de datos listas para usar.
class GestorDeDatos:

    ## @brief Crea y devuelve un mapa de publicaciones (ID -> Publicacion)
    #  con entradas de prueba basadas en publicaciones reales.
    #
    #  @return Un diccionario (Dict[str, Publicacion]) poblado con datos.
    @staticmethod
    def cargar_publicaciones_de_prueba():
        publicaciones = {}

        # --- 1. Creación de Autores ---

        # Científicos y Físicos
        aEinstein = Autor("Albert","Einstein","Universidad de Berna")
        aWatson = Autor("James","Watson","Universidad de Cambridge")
        aCrick = Autor("Francis","Crick","Universidad de Cambridge")
        aDarwin = Autor("Charles","Darwin","N/A")
        aHawking = Autor("Stephen","Hawking","Universidad de Cambridge")
        aCurie = Autor("Marie","Curie","Universidad de París")
        aNewton = Autor("Isaac","Newton","Universidad de Cambridge")

        # Informáticos y Matemáticos
        aTuring = Autor("Alan","Turing","Universidad de Cambridge")
        aKnuth = Autor("Donald","Knuth","Universidad de Stanford")
        aAho = Autor("Alfred","Aho","Bell Labs")
        aUllman = Autor("Jeffrey","Ullman","Universidad de Stanford")
        aSethi = Autor("Ravi","Sethi","Bell Labs")
        aKernighan = Autor("Brian","Kernighan","Bell Labs")
        aRitchie = Autor("Dennis","Ritchie","Bell Labs")
        aPike = Autor("Rob","Pike","Bell Labs")
        aGamma = Autor("Erich","Gamma","N/A")
        aHelm = Autor("Richard","Helm","N/A")
        aJohnson = Autor("Ralph","Johnson","N/A")
        aVlissides = Autor("John","Vlissides","N/A")
        aCodd = Autor("Edgar F.","Codd","IBM Research")
        aShannon = Autor("Claude","Shannon","Bell Labs")
        aDijkstra = Autor("Edsger","Dijkstra","Varios")

        # Otros
        aHinton = Autor("Geoffrey","Hinton","University of Toronto")
        aLeCun = Autor("Yann","LeCun","New York University")
        aBengio = Autor("Yoshua","Bengio","Université de Montréal")

        # Autores adicionales para los artículos
        aKrizhevsky = Autor("Alex","Krizhevsky","University of Toronto")
        aSutskever = Autor("Ilya","Sutskever","University of Toronto")
        aBottou = Autor("Léon","Bottou","AT&T Labs")
        aHaffner = Autor("Patrick","Haffner","AT&T Labs")
        aDucharme = Autor("Réjean","Ducharme","Université de Montréal")
        aVincent = Autor("Pascal","Vincent","Université de Montréal")
        aGoodfellow = Autor("Ian","Goodfellow","Université de Montréal")
        aCourville = Autor("Aaron","Courville","Université de Montréal")

        # Desarrollo de Software
        aMartin = Autor("Robert C.","Martin","N/A")
        aHunt = Autor("Andrew","Hunt","N/A")
        aThomas = Autor("David","Thomas","N/A")

        # ... (otros autores)
        aSmith = Autor("Adam","Smith","N/A")
        aKeynes = Autor("John Maynard","Keynes","Universidad de Cambridge")
        aMachiavelli = Autor("Niccolò","Machiavelli","N/A")
        aSunTzu = Autor("Sun","Tzu","N/A")
        aPage = Autor("Larry","Page","Universidad de Stanford")
        aBrin = Autor("Sergey","Brin","Universidad de Stanford")
        aMcCarthy = Autor("John","McCarthy","MIT")
        aDennard = Autor("Robert","Dennard","IBM")
        aCormen = Autor("Thomas H.","Cormen","MIT")
        aLeiserson = Autor("Charles E.","Leiserson","MIT")
        aRivest = Autor("Ronald L.","Rivest","MIT")
        aStein = Autor("Clifford","Stein","Dartmouth")
        aHuffman = Autor("David A.","Huffman","MIT")
        aAbelson = Autor("Harold","Abelson","MIT")
        aSussman = Autor("Gerald Jay","Sussman","MIT")
        aMetcalfe = Autor("Robert","Metcalfe","Xerox PARC")
        aThompson = Autor("Ken","Thompson","Bell Labs")
        aOrwell = Autor("George","Orwell","N/A")
        aBrooks = Autor("Frederick","Brooks","IBM")

        # --- 2. Creación de Publicaciones ---

        # ----- LIBROS -----

        lib1 = Libro(
            "Clean Code: A Handbook of Agile Software Craftsmanship",
            "LIB-001",
            [aMartin],
            ["software","agile","craftsmanship","coding"],
            "200808",
            "Prentice Hall"
        )
        publicaciones[lib1.get_id()] = lib1

        lib2 = Libro(
            "The Pragmatic Programmer: Your Journey to Mastery",
            "LIB-002",
            [aHunt,aThomas],
            ["programming","career","pragmatic","software"],
            "199910",
            "Addison-Wesley"
        )
        publicaciones[lib2.get_id()] = lib2

        lib3 = Libro(
            "Design Patterns: Elements of Reusable Object-Oriented Software",
            "LIB-003",
            [aGamma,aHelm,aJohnson,aVlissides],
            ["design","patterns","gof","oop"],
            "199410",
            "Addison-Wesley"
        )
        publicaciones[lib3.get_id()] = lib3

        art_gof_shared = ArticuloEnRevista(
            "Design patterns for object-oriented hypermedia",
            "ART-GOF-S",
            [aGamma,aHelm],
            ["design","patterns","hypermedia"],
            "199603",
            6.7,
            "ACM Computing Surveys"
        )
        publicaciones[art_gof_shared.get_id()] = art_gof_shared

        lib4 = Libro(
            "The Art of Computer Programming, Vol. 1: Fundamental Algorithms",
            "LIB-004",
            [aKnuth],
            ["algorithms","data structures","math"],
            "196801",
            "Addison-Wesley"
        )
        publicaciones[lib4.get_id()] = lib4

        lib5 = Libro(
            "The C Programming Language",
            "LIB-005",
            [aKernighan,aRitchie],
            ["c","programming","k&r","systems"],
            "197802",
            "Prentice Hall"
        )
        publicaciones[lib5.get_id()] = lib5

        lib_kp_shared = Libro(
            "The Practice of Programming",
            "LIB-KP-S",
            [aKernighan,aPike],
            ["programming","practice","software","tools"],
            "199902",
            "Addison-Wesley"
        )
        publicaciones[lib_kp_shared.get_id()] = lib_kp_shared

        art_unix = ArticuloEnRevista(
            "The UNIX Time-Sharing System",
            "ART-013",
            [aRitchie,aThompson],
            ["unix","os","systems","c"],
            "197407",
            10.1,
            "Communications of the ACM"
        )
        publicaciones[art_unix.get_id()] = art_unix

        lib6 = Libro(
            "Compilers: Principles, Techniques, and Tools (Dragon Book)",
            "LIB-006",
            [aAho,aSethi,aUllman],
            ["compilers","dragon book","parsing","cs"],
            "198601",
            "Addison-Wesley"
        )
        publicaciones[lib6.get_id()] = lib6

        lib_dragon_shared = Libro(
            "Principles of Compiler Design",
            "LIB-DRG-S",
            [aAho,aUllman],
            ["compilers","parsing","cs"],
            "197701",
            "Addison-Wesley"
        )
        publicaciones[lib_dragon_shared.get_id()] = lib_dragon_shared

        lib7 = Libro(
            "On the Origin of Species",
            "LIB-007",
            [aDarwin],
            ["evolution","biology","natural selection"],
            "185911",
            "John Murray"
        )
        publicaciones[lib7.get_id()] = lib7

        lib8 = Libro(
            "A Brief History of Time",
            "LIB-008",
            [aHawking],
            ["cosmology","physics","time","black holes"],
            "198804",
            "Bantam Dell"
        )
        publicaciones[lib8.get_id()] = lib8

        lib9 = Libro(
            "Philosophiæ Naturalis Principia Mathematica",
            "LIB-009",
            [aNewton],
            ["physics","math","gravity","classical mechanics"],
            "168707",
            "N/A"
        )
        publicaciones[lib9.get_id()] = lib9

        lib10 = Libro(
            "Radio-active substances",
            "LIB-010",
            [aCurie],
            ["radioactivity","chemistry","polonium","radium"],
            "190401",
            "Chemical News"
        )
        publicaciones[lib10.get_id()] = lib10

        lib11 = Libro(
            "The Wealth of Nations",
            "LIB-011",
            [aSmith],
            ["economics","capitalism","free market"],
            "177603",
            "W. Strahan"
        )
        publicaciones[lib11.get_id()] = lib11

        lib12 = Libro(
            "The General Theory of Employment, Interest and Money",
            "LIB-012",
            [aKeynes],
            ["economics","macroeconomics","keynesian"],
            "193602",
            "Macmillan"
        )
        publicaciones[lib12.get_id()] = lib12

        lib13 = Libro(
            "The Prince",
            "LIB-013",
            [aMachiavelli],
            ["politics","philosophy","strategy"],
            "153201",
            "Antonio Blado"
        )
        publicaciones[lib13.get_id()] = lib13

        lib14 = Libro(
            "The Art of War",
            "LIB-014",
            [aSunTzu],
            ["strategy","war","philosophy"],
            "191001",
            "N/A"
        )
        publicaciones[lib14.get_id()] = lib14

        lib15 = Libro(
            "Introduction to Algorithms (CLRS)",
            "LIB-015",
            [aCormen,aLeiserson,aRivest,aStein],
            ["algorithms","clrs","cs","data structures"],
            "199001",
            "MIT Press"
        )
        publicaciones[lib15.get_id()] = lib15

        lib16 = Libro(
            "Structure and Interpretation of Computer Programs (SICP)",
            "LIB-016",
            [aAbelson,aSussman],
            ["sicp","lisp","scheme","cs","mit"],
            "198501",
            "MIT Press"
        )
        publicaciones[lib16.get_id()] = lib16

        lib17 = Libro(
            "1984",
            "LIB-017",
            [aOrwell],
            ["dystopia","fiction","politics","surveillance"],
            "194906",
            "Secker & Warburg"
        )
        publicaciones[lib17.get_id()] = lib17

        # ----- ARTÍCULOS EN REVISTA -----

        art1 = ArticuloEnRevista(
            "On Computable Numbers, with an Application to the Entscheidungsproblem",
            "ART-001",
            [aTuring],
            ["turing machine","computation","math","entscheidungsproblem"],
            "193701",
            9.5,
            "Proceedings of the London Mathematical Society"
        )
        publicaciones[art1.get_id()] = art1

        art2 = ArticuloEnRevista(
            "A Relational Model of Data for Large Shared Data Banks",
            "ART-002",
            [aCodd],
            ["database","relational","sql","data model"],
            "197006",
            12.8,
            "Communications of the ACM"
        )
        publicaciones[art2.get_id()] = art2

        art3 = ArticuloEnRevista(
            "A Mathematical Theory of Communication",
            "ART-003",
            [aShannon],
            ["information theory","bits","entropy","communication"],
            "194807",
            15.2,
            "Bell System Technical Journal"
        )
        publicaciones[art3.get_id()] = art3

        art4 = ArticuloEnRevista(
            "Go To Statement Considered Harmful",
            "ART-004",
            [aDijkstra],
            ["structured programming","goto","cs","coding"],
            "196803",
            5.1,
            "Communications of the ACM"
        )
        publicaciones[art4.get_id()] = art4

        art5 = ArticuloEnRevista(
            "Zur Elektrodynamik bewegter Körper (On the Electrodynamics of Moving Bodies)",
            "ART-005",
            [aEinstein],
            ["relativity","physics","electrodynamics","e=mc2"],
            "190509",
            22.7,
            "Annalen der Physik"
        )
        publicaciones[art5.get_id()] = art5

        art6 = ArticuloEnRevista(
            "Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid",
            "ART-006",
            [aWatson,aCrick],
            ["dna","biology","double helix","genetics"],
            "195304",
            42.8,
            "Nature"
        )
        publicaciones[art6.get_id()] = art6

        art7 = ArticuloEnRevista(
            "The Anatomy of a Large-Scale Hypertextual Web Search Engine",
            "ART-007",
            [aPage,aBrin],
            ["google","search engine","pagerank","internet"],
            "199804",
            18.5,
            "Computer Networks and ISDN Systems"
        )
        publicaciones[art7.get_id()] = art7

        art8 = ArticuloEnRevista(
            "Recursive Functions of Symbolic Expressions and Their Computation by Machine (LISP)",
            "ART-008",
            [aMcCarthy],
            ["lisp","programming language","ai","functional"],
            "196004",
            10.2,
            "Communications of the ACM"
        )
        publicaciones[art8.get_id()] = art8

        art9 = ArticuloEnRevista(
            "Computing Machinery and Intelligence (Turing Test)",
            "ART-009",
            [aTuring],
            ["ai","turing test","intelligence","philosophy"],
            "195010",
            14.1,
            "Mind"
        )
        publicaciones[art9.get_id()] = art9

        art10 = ArticuloEnRevista(
            "An integrated circuit memory (RAM)",
            "ART-010",
            [aDennard],
            ["ram","memory","semiconductor","electronics"],
            "197104",
            8.8,
            "IEEE Journal of Solid-State Circuits"
        )
        publicaciones[art10.get_id()] = art10

        art11 = ArticuloEnRevista(
            "A Method for the Construction of Minimum Redundancy Codes (Huffman)",
            "ART-011",
            [aHuffman],
            ["compression","huffman","coding","data"],
            "195209",
            7.3,
            "Proceedings of the IRE"
        )
        publicaciones[art11.get_id()] = art11

        art12 = ArticuloEnRevista(
            "Ethernet: Distributed Packet Switching for Local Computer Networks",
            "ART-012",
            [aMetcalfe],
            ["ethernet","networking","lan","packets"],
            "197607",
            11.9,
            "Communications of the ACM"
        )
        publicaciones[art12.get_id()] = art12

        art16 = ArticuloEnRevista(
            "The Mythical Man-Month",
            "ART-016",
            [aBrooks],
            ["software engineering","management","brooks law"],
            "197501",
            13.0,
            "Addison-Wesley"
        )
        publicaciones[art16.get_id()] = art16

        # Otros artículos con varios autores, algunos de ellos compartidos

        # ARTÍCULO 1 (3 autores: LeCun, Bengio, Hinton)
        artIA1 = ArticuloEnRevista(
            "Deep Learning",
            "ART-IA-001",
            [aLeCun,aBengio,aHinton],
            ["deep learning","ai","machine learning","review"],
            "201505",
            42.7,
            "Nature"
        )
        publicaciones[artIA1.get_id()] = artIA1

        # ARTÍCULO 2 (3 autores: Krizhevsky, Sutskever, Hinton)
        # Comparte: Hinton (con ART-IA-001)
        artIA2 = ArticuloEnRevista(
            "ImageNet Classification with Deep Convolutional Neural Networks",
            "ART-IA-002",
            [aKrizhevsky,aSutskever,aHinton],
            ["imagenet","cnn","deep learning","computer vision"],
            "201212",
            18.0,
            "Advances in Neural Information Processing Systems (NIPS)"
        )
        publicaciones[artIA2.get_id()] = artIA2

        # ARTÍCULO 3 (4 autores: LeCun, Bottou, Bengio, Haffner)
        # Comparte: LeCun, Bengio (con ART-IA-001)
        artIA3 = ArticuloEnRevista(
            "Gradient-Based Learning Applied to Document Recognition",
            "ART-IA-003",
            [aLeCun,aBottou,aBengio,aHaffner],
            ["cnn","mnist","lenet","ocr"],
            "199811",
            10.5,
            "Proceedings of the IEEE"
        )
        publicaciones[artIA3.get_id()] = artIA3

        # ARTÍCULO 4 (3 autores: Bengio, Ducharme, Vincent)
        # Comparte: Bengio (con ART-IA-001 y ART-IA-003)
        artIA4 = ArticuloEnRevista(
            "A Neural Probabilistic Language Model",
            "ART-IA-004",
            [aBengio,aDucharme,aVincent],
            ["nlp","language model","neural networks"],
            "200303",
            15.2,
            "Journal of Machine Learning Research (JMLR)"
        )
        publicaciones[artIA4.get_id()] = artIA4

        # ARTÍCULO 5 (3+ autores: Goodfellow, Courville, Bengio, ...)
        # Comparte: Bengio (con ART-IA-001, ART-IA-003, ART-IA-004)
        artIA5 = ArticuloEnRevista(
            "Generative Adversarial Networks",
            "ART-IA-005",
            [aGoodfellow,aCourville,aBengio],
            ["gan","generative models","ai","unsupervised"],
            "201406",
            19.1,
            "Advances in Neural Information Processing Systems (NIPS)"
        )
        publicaciones[artIA5.get_id()] = artIA5

        # --- INICIO: 5 Artículos **INVENTADOS** con Palabras Clave Compartidas ---

        artOpt1 = ArticuloEnRevista(
            "Dropout: A Simple Way to Prevent Neural Networks from Overfitting",
            "ART-OPT-001",
            [aHinton,aSutskever,
             Autor("Nitish","Srivastava","University of Toronto"),
             aKrizhevsky],  # Reutilizado de ART-IA-002
            ["dropout","regularization","neural networks","optimization"],
            "201401",
            17.5,
            "Journal of Machine Learning Research (JMLR)"
        )
        publicaciones[artOpt1.get_id()] = artOpt1

        artOpt2 = ArticuloEnRevista(
            "On the importance of initialization and momentum in deep learning",
            "ART-OPT-002",
            [aSutskever,
             Autor("James","Martens","University of Toronto"),
             aHinton],
            ["momentum","initialization","neural networks","optimization"],
            "201302",
            16.2,
            "Proceedings of the 30th ICML"
        )
        publicaciones[artOpt2.get_id()] = artOpt2

        artOpt3 = ArticuloEnRevista(
            "Stochastic Gradient Descent Tricks",
            "ART-OPT-003",
            [aBottou,aLeCun,
             Autor("Frank","Rosenblatt","Cornell")],  # (Autor histórico)
            ["sgd","tricks","neural networks","optimization"],
            "201201",
            11.8,
            "Neural Networks: Tricks of the Trade"
        )
        publicaciones[artOpt3.get_id()] = artOpt3

        artOpt4 = ArticuloEnRevista(
            "Gradient-based learning in recurrent neural networks",
            "ART-OPT-004",
            [aBengio,aVincent,
             Autor("M.","Simard","Université de Montréal")],
            ["rnn","vanishing gradient","neural networks","optimization"],
            "199401",
            9.1,
            "IEEE Transactions on Neural Networks"
        )
        publicaciones[artOpt4.get_id()] = artOpt4

        artOpt5 = ArticuloEnRevista(
            "A Unified View of Optimization Algorithms",
            "ART-OPT-005",
            [aLeCun,aBengio,aHinton],  # <-- El trío
            ["review","adam","rmsprop","neural networks","optimization"],
            "201811",
            25.3,
            "Communications of the ACM"
        )
        publicaciones[artOpt5.get_id()] = artOpt5

        # --- FIN: 5 Artículos con Palabras Clave Compartidas ---

        return publicaciones
