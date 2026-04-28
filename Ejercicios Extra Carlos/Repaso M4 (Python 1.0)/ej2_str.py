matricula = "1234ABC"

numeros = matricula[:4]
letras = matricula[4:]

if numeros.isdigit() and letras.isalpha() and letras.isupper():
    print("Matrícula válida")
else:
    print("Matrícula no válida")