comentario = "MUY BUENO!!!"

if comentario.isupper():
    print("El comentario está en mayúsculas")

if comentario.islower():
    print("El comentario está en minúsculas")

comentario_limpio = comentario.replace("!", "").replace(".", "")
palabras = comentario_limpio.split()

print("Comentario limpio:", comentario_limpio)
print("Palabras:", palabras)