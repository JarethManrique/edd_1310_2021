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
            print(f"{curr_node.data} -> ", end="")
            curr_node = curr_node.next
        print("")

    def remove(self, value):
        curr_node = self.__head
        if self.__head.data == value:       # Si se quiere eliminar el head
            self.__head = self.__head.next  # Head se vuelve el siguiente nodo
        else:
            anterior = None
            while curr_node.data != value and curr_node.next != None:
                anterior = curr_node
                curr_node = curr_node.next
            if curr_node.data == value:
                #print("Actual: ", anterior.data)
                anterior.next = curr_node.next
            else:
                print("El dato no existe en la lista")

    def preppend(self, value):
        nuevo = Nodo(value, self.__head)
        self.__head = nuevo

    def tail(self):
        curr_node = self.__head
        while curr_node.next != None:
            curr_node = curr_node.next
        return curr_node

    def get(self , position=None):#por defecto regrese el ultimo
        count=0
        dat=None
        if position == None :
            dat=self.tail().data
        else:
            curr_node = self.__head
            while count != position and curr_node.next != None:
                curr_node = curr_node.next
                count += 1
            if(count==position):
                dat = curr_node.data
            else:
                dat = "ERROR: Esa posición no existe en la lista"
        return dat

#    def add_before(reference_value, value):
