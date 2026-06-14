print("Programa 3")
print("Detector de número positivo, negativo o cero.")
alumno = input("Ingrese su nombre: ")
numero = float(input("Ingrese un valor para determinar que es"))
if numero > 0:
    print(alumno, "el número", numero, "es positivo.")
elif numero < 0:
    print(alumno, "el número", numero, "es negativo.")   
else:
    print(alumno, "el número", numero, "es cero.")