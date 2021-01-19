class NodoArbol:
    def __init__( self, value, left=None, right=None ):
        self.data = value
        self.left = left
        self.right = right

def preOrden(leaf):
    if leaf:
        print(leaf.data, end=" --> ")
        preOrden(leaf.left)
        preOrden(leaf.right)

def inOrden(leaf):
    if leaf:
        inOrden(leaf.left)
        print(leaf.data, end=" --> ")
        inOrden(leaf.right)


def postOrden(leaf):
    if leaf:
        postOrden(leaf.left)
        postOrden(leaf.right)
        print(leaf.data, end=" --> ")


def main1():
    arbol = NodoArbol('+', NodoArbol('-', NodoArbol('5'), NodoArbol('4')), NodoArbol('*', NodoArbol('3'), NodoArbol('2')) )
    print("\n--------ARBOL #1--------")
    print("\nIn Order:")
    inOrden(arbol)
    print("\n\nPost Orden:")
    postOrden(arbol)
    print("\n\nPre Order:")
    preOrden(arbol)

def main2():
    arbol = NodoArbol(40, NodoArbol(30, NodoArbol(25), NodoArbol(35)), NodoArbol(50, NodoArbol(45), NodoArbol(60)) )
    print("\n\n--------ARBOL #2--------")
    print("\nIn Order:")
    inOrden(arbol)
    print("\n\nPost Orden:")
    postOrden(arbol)
    print("\n\nPre Order:")
    preOrden(arbol)

main1()
main2()
