notas = [7, 9, 5, 10, 6]

notas.sort() # Ordena de menor a mayor // list.sort(reverse = True)
nota_mas_baja = notas.pop(0) # Extrae y elimina el elemento en la posicion 0

notas.reverse() # Invierte el orden (no ordena)

print("Nota más baja eliminada:", nota_mas_baja)
print("Ranking de notas:", notas)