from Stack import Stack

def borrarPM( stack , pos = 1 ):
    const = round( (stack.lenght() + pos) / 2)

    if pos != const:
        ultimoVal = stack.peek()
        stack.pop()
        borrarPM( stack, pos = pos + 1 )
        stack.push(ultimoVal)
    else:
        print( f"Valor en medio de la pila = {stack.peek()}" )
        stack.pop()


def main():
    pila = Stack()
    pila.push("1")
    pila.push("2")
    pila.push("3")
    pila.push("4") # Valor Medio
    pila.push("5")
    pila.push("6")
    pila.push("7")

    print("-------- PILA ORIGINAL --------")
    pila.to_string()

    borrarPM( pila )
    print("-------- PILA MODIFICADA --------")
    pila.to_string()


main()
