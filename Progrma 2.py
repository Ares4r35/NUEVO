print("Programa2")
print("Verificador de aprobacion de examenes")

nombre = input("Ingrese su nombre: ")
materia = input("Ingrese la materia: ")
nota = float(input("Ingrese su nota: "))
if nota >= 70:
    print(f"Felicidades {nombre}, has aprobado la materia de {materia} con una nota de {nota} puntos.")
elif nota >= 50:
    print(f"{nombre}, has aprobado la materia de {materia} con una nota de {nota} puntos.")
else:
    print(f"{nombre}, has reprobado la materia de {materia} con una nota de {nota} puntos. ¡Sigue esforzándote!")

