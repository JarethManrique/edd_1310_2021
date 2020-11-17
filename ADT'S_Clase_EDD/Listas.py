class Nodo:
    def __init__( self, value, siguiente=None):
        self.data = value     # Falta emcapsulamiento
        self.next = siguiente

class LinkedList:
    def __init__(self):     # Constructor
        self.__head = None

    def is_empty(self):     # Si head = None la lista está vacía
        return self.__head == None

    def append(self, value):    # Agrega un valor nuevo
        nuevo = Nodo(value)
        if self.__head == None:
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.next != None:   # Está verificando si ya llegaron al final
                curr_node = curr_node.next
            curr_node.next = nuevo

    def transversal(self):      # Recorrido de toda la lista y lo imprime
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} ->", end="")
            curr_node = curr_node.next
        print("")
    def remove(self, value):
        curr_node = self.__head
        while curr_node != value and curr_node.next != None:
            curr_node = curr_node.next
        if curr_node.data == value:
