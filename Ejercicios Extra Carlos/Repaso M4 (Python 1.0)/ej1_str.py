emails = ["ana.ventas@empresa.com", "luis@empresa.com", "rrhh.madrid@empresa.com"]

contador_ventas = 0

for email in emails:
    if email.find("@") != -1:
        usuario, dominio = email.split("@")

        nuevo_email = email.replace("empresa.com", "nuevaempresa.com")

        if usuario.count("ventas") > 0:
            contador_ventas += 1

        print("Usuario:", usuario)
        print("Dominio:", dominio)
        print("Nuevo email:", nuevo_email)
        print()

print("Correos del departamento de ventas:", contador_ventas)