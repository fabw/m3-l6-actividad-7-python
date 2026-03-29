numero = -1
while numero <= 0 or numero > 100:
    numero = int(input("Ingrese un número: "))

    if numero <= 0 or numero > 100:
        print("No es posible realizarlo")

if numero % 2 == 0:
    print("Usted ha ingresado un numero par y los números pares siguientes son:")

    for i in range(numero + 2, 101, 2):
        print(i, end=" ")

else:
    print("Usted ha ingresado un número impar y los números impares siguientes son:")

    for i in range(numero + 2, 100, 2):
        print(i, end=" ")