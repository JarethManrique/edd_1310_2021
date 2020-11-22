from Listas import DoubleLinkedList

l=DoubleLinkedList()
print(f"\n¿La lista L está vacía?: { l.is_empty() } ")
print(f"El número de elementos de la lista L son: {l.get_size()}\n")

print("Agregamos: 10,15,10,20,30,10,40,50\n")
l.append(10)
l.append(15)
l.append(10)
l.append(20)
l.append(30)
l.append(10)
l.append(40)
l.append(50)

print(f"¿La lista L está vacía?: { l.is_empty() } ")
print(f"El número de elementos de la lista L son: {l.get_size()}\n")

print("La lista es: ")
l.transversal()

print("\n>>>Conocer posición del número 20 a partir de Head<<<")
print(f"La posicion del numero 20 desde Head es: {l.find_from_head(20)} ")

print("\n>>>Conocer posición del número 20 a partir de Tail<<<")
print(f"La posicion del numero 20 desde Tail es: {l.find_from_tail(20)} ")

print("\n>>>Se elimina el numero 15 a partir de Head<<<")
l.remove_from_head(15)
print("La lista ahora es: ")
l.transversal()

print("\n>>>Se elimina el número 10 a partir de Tail (2 veces)<<<")
l.remove_from_tail(10)
l.remove_from_tail(10)
print("La lista ahora es: ")
l.transversal()

print("\n>>>Conocer el tamaño de la lista L<<<")
print(f"El número de elementos de la lista L son: {l.get_size()}")

print("\n>>>Se intenta remover un valor que no esta en la lista (Remover 25)<<<")
l.remove_from_head(25)

print("\n>>>Recorrido de la lista desde Head (recorrido normal)<<<")
l.transversal()

print("\n>>>Recorrido de la lista comenzando desde Tail (recorrido inverso)<<<")
l.reverse_transversal()
