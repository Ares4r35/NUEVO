nombre = input("Ingrese su nombre completo: ")
print(f"Bienvenido, {nombre}")

try:
    edad = int(input("Cuántos años tienes: "))
except ValueError:
    print("Debes ingresar un número válido para la edad.")
    edad = 0


def acceso_permitido(edad):
    if edad >= 18:
        print("Eres mayor de edad, puedes acceder a esta opción.")
        return True
    else:
        print("Eres menor de edad, no puedes acceder a esta opción.")
        return False


if acceso_permitido(edad):
    def funcion_principal(edad):
        print("Has logrado avanzar al siguiente nivel...")
        # Aquí va el código de la función que quieres permitir
    direccion = input("Ingrese su ciudad: ")
    print(f"{nombre}, de {direccion}, me prodias indicar el nombre de la calle donde vives")

    funcion_principal(print("Función principal ejecutada con éxito."))