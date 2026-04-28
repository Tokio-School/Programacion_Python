respuestas = [
    "SI, estoy satisfecho",
    "no, el servicio fue lento",
    "SI, volvería a comprar",
    "No, precio alto",
    "si, buena atención"
]

comentarios = []
afirmativas = 0
negativas = 0

for respuesta in respuestas:
    partes = respuesta.split(",")
    decision = partes[0].replace(" ", "")
    comentario = partes[1].replace(" ", "", 1)

    if decision.upper() == "SI":
        afirmativas += 1
    elif decision.lower() == "no":
        negativas += 1

    comentarios.append(comentario)

comentarios.sort()

texto_comentarios = " / ".join(comentarios)

print("Respuestas afirmativas:", afirmativas)
print("Respuestas negativas:", negativas)
print("Comentarios ordenados:", comentarios)
print("Texto final:", texto_comentarios)