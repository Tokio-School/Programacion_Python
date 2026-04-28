codigos = ["DESC10", "promo20", "OFERTA", "VIP99", "gratis"]

codigos_con_numero = []
codigos_sin_numero = []

ultimo = codigos.pop()
codigos.append("BLACK50")

for codigo in codigos:
    tiene_numero = False

    for caracter in codigo:
        if caracter.isdigit():
            tiene_numero = True

    if tiene_numero:
        codigos_con_numero.append(codigo)
    else:
        codigos_sin_numero.append(codigo)

codigos_con_numero.sort()
codigos_sin_numero.sort()

resultado = codigos_con_numero + codigos_sin_numero

texto_final = " - ".join(resultado)

print("Código eliminado:", ultimo)
print("Códigos con número:", codigos_con_numero)
print("Códigos sin número:", codigos_sin_numero)
print("Texto final:", texto_final)