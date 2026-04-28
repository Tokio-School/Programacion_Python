usuarios = [" ANA123 ", "luis", "MARTA99", "pepe_45", "SOFIA"]

usuarios_con_numeros = []
usuarios_sin_numeros = []

for usuario in usuarios:
    usuario = usuario.replace(" ", "")

    if usuario.isalnum():
        tiene_numero = False

        for caracter in usuario:
            if caracter.isdigit():
                tiene_numero = True

        usuario = usuario.lower()

        if tiene_numero:
            usuarios_con_numeros.append(usuario)
        else:
            usuarios_sin_numeros.append(usuario)

usuarios_con_numeros.sort()
usuarios_sin_numeros.sort()

resultado = usuarios_sin_numeros + usuarios_con_numeros

print("Usuarios válidos:", ", ".join(resultado))