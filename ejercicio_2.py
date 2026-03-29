notas = []

for i in range(1, 6):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

print("Notas ingresadas:", notas)
print("Nota media:", sum(notas) / len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))