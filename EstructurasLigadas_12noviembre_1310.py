class Nodo:
    def __init__( self , dato ):
        self.dato = dato
        self.siguiente = None


# ejemplo 1
a = Nodo( 12 )
print( a.dato )
print( a.siguiente )

# ejemplo 2
a.siguiente = Nodo( 20 )

#ejemplo 3

a.siguiente.siguiente=Nodo(30)

#ejemplo 4
a.siguiente.siguiente.siguiente=Nodo(40)

#ejemplo 5
a.siguiente.siguiente.siguiente.siguiente=Nodo(50)

#Eliminando nodo 30 ejemplo 6

a.siguiente.siguiente=a.siguiente.siguiente.siguiente

# ejemplo 7
a.siguiente.siguiente
.dato = 45

#EJEMPLO 8 insertar dato



curr_node = a
print(curr_node.dato , "-->" , end="")
while( curr_node.siguiente != None ):
    curr_node = curr_node.siguiente
    print(curr_node.dato, "-->" , end="")
print("")
