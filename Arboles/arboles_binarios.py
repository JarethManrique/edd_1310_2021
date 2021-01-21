class NodoArbol:
    def __init__(self, value, left=None,right=None):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, value):
        # REGLA 1
        if self.__root == None:
            self.__root = NodoArbol(value,None,None)
        # REGLA 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe, no se puede ingresar")
        elif value < nodo.data:
            # REGLA 1
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            # REGLA 2
            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right, value)
        # Y TAN TAN

    def __recorrido_in(self, nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=", ")
            self.__recorrido_in(nodo.right)

    def __recorrido_pos(self, nodo):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end=", ")

    def __recorrido_pre(self, nodo):
        if nodo:
            print(nodo.data, end=", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def transversal(self,format="inorden"):
        if format == "inorden":
            print("inorden")
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("preorden")
            self.__recorrido_pre(self.__root)
        elif format == "posorden":
            print("posorden")
            self.__recorrido_pos(self.__root)
        else:
            print("Error, formato incompatible")
        print()

    def search(self, value):
        if self.__root == None:
            return None
        else:
            return self.__search(self.__root, value)

    def __search(self, nodo, value):
        if nodo == None: # Vacío?
            return None
        elif nodo.data == value:
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            return self.__search(nodo.left, value)
        else:
            return self.__search(nodo.right, value)

    def remove(self, value):
        encontrado = self.search(value)
        # CASO 1
        if encontrado.left == None and encontrado.right == None:
            print("Eliminando ", encontrado.data)
            encontrado = None
        # CASO 2
        elif (encontrado.left != None and encontrado.right == None) or \
             (encontrado.left == None and encontrado.right != None):
             print("A eliminar: ", encontrado.data)
