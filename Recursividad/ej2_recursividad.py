def cuentaReg( num ):
    if num >= 0:
        if num == 0:
            print("0")
        else:
            print( num )
            cuentaReg( num - 1 )

    else:
        print("Este no es un numero positivo")


def main():
    cuentaReg( 10 )

main()
