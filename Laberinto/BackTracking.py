from Array2D import Array2D
from Stack import Stack

class Laberinto_ADT:
    """
     E:ENTRADA | S:SALIDA | 0:PASILLO | 1:PARED |
     Pasillo es una tupla ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
     Entrada en una tupla (5,2)
     Salida en una tupla (2,5)
    """
    def __init__(self, rows, cols, pasillos, entrada, salida ):
        self.__laberinto = Array2D(rows,cols, "▓▓")
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1],"░░")
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino = Stack()
        self.__previa = none
        self.__

    def to_string(self):
        self.__laberinto.to_string()

    """
    Establece la ENTRADA poniendo una >E< en la matriz
    """
    def set_entrada(self, ren, col):
        # Terminar la validación de las coordenadas
        self.__laberinto.set_item(ren,col,"E ")

    """
    Establece la SALIDA poniendo una >S< en la matriz
    """
    def set_salida(self, ren, col):
        # Terminar la validación de las coordenadas
        self.__laberinto.set_item(ren,col,"S ")

    def es_salida ( self, ren, col ):
        return self.__laberinto.get_item(ren, col) == "S"

    def buscar_entrada(self):
        encontrado = false
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range (self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(renglon,columna) == "E":
                    self.__camino.push(tuple(renglon,columna))
                    encontrado = True
        return encontrado

    def set_previa(self, pos_previa):
        self.__previa = pos_previa

    def get_prevoa(self):
        return self.__previa

    def resolver(self):
        # Aplicar reglas
