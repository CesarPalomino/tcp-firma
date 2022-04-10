import nacl.utils

cant = 1

while cant > -1:
    cant = int(input("Cantidad de numeros aleatorios: "))

    randoms= nacl.utils.random(cant)

    print("Numeros aleatorios: " + str(randoms))

    print("Numeros hexadecimal: ")
    print(randoms.hex())

    print("Numeros decimal: ")
    for i in randoms:
        print(str(i)+ " ",end= "")

    print()
    





