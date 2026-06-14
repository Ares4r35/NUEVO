print ("Programa 4")
print ("Solicitar usuario y contraseña.")
print ("Ingrese su usuario y contraseña para iniciar sesión")
usuario = input("Usuario: ")
contraseña = int(input("Contraseña: "))
if usuario == "admin" and contraseña == 1234:
    print("Bienvenido", usuario)
elif usuario == "admin" and contraseña != 1234:
    print("Contraseña incorrecta")
elif usuario != "admin" and contraseña == 1234:
    print("Usuario incorrecto")
else:    print("Usuario y contraseña incorrectos")