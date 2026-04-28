texto = "Hoy aprendí #Python y #IA en clase #Python"

cantidad_hashtags = texto.count("#")
primera_posicion = texto.index("#")

palabras = texto.split()
hashtags = []

for palabra in palabras:
    if palabra.find("#") == 0:
        hashtags.append(palabra)

print("Cantidad de hashtags:", cantidad_hashtags)
print("Primera posición de hashtag:", primera_posicion)
print("Hashtags encontrados:", hashtags)