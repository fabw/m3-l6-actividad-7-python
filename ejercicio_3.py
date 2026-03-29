meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numero_mes = int(input("Ingrese un número de mes: "))

if numero_mes >= 1 and numero_mes <= 12:
    print("Mes:", meses[numero_mes - 1])
    print("Días:", dias_por_mes[numero_mes - 1])
else:
    print("Número de mes no válido")