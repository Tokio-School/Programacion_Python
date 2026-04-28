frase = "python es genial y python es potente"

veces = frase.count("python")
posicion = frase.find("python") # posicion = frase.find("python", 5) -> str.find(sub, start, end)
palabras = frase.split()
frase_con_guiones = "-".join(palabras)

print("Veces que aparece python:", veces)
print("Primera posición:", posicion)
print("Frase con guiones:", frase_con_guiones)