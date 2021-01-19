class NodoArbol:
    def __init__( self, value, left=None, right=None ):
        self.data = value
        self.left = left
        self.right = right

def preFija(leaf):
    if leaf:
        print(leaf.data, end=" --> ")
        preFija(leaf.left)
        preFija(leaf.right)

def postFija(leaf):
    if leaf:
        postFija(leaf.left)
        postFija(leaf.right)
        print(leaf.data, end=" --> ")

def inFija(leaf):
    if leaf:
        inFija(leaf.left)
        print(leaf.data, end=" --> ")
        inFija(leaf.right)

def main1():
    arbol = NodoArbol('+', NodoArbol('-', NodoArbol('5'), NodoArbol('4')), NodoArbol('*', NodoArbol('3'), NodoArbol('2')) )
    print("\n--------ARBOL #1--------")
    print("\nIn Order:")
    inFija(arbol)
    print("\n\nPost Orden:")
    postFija(arbol)
    print("\n\nPre Order:")
    preFija(arbol)

def main2():
    arbol = NodoArbol(40, NodoArbol(30, NodoArbol(25), NodoArbol(35)), NodoArbol(50, NodoArbol(45), NodoArbol(60)) )
    print("\n\n--------ARBOL #2--------")
    print("\nIn Order:")
    inFija(arbol)
    print("\n\nPost Orden:")
    postFija(arbol)
    print("\n\nPre Order:")
    preFija(arbol)

main1()
main2()
