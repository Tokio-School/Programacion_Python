tareas = ["Comprar", "Estudiar", "Limpiar"]

tareas.append("Hacer ejercicio")
tareas.insert(0, "Enviar trabajo")
tareas.remove("Comprar")

posicion = tareas.index("Estudiar")

print("Tareas actuales:", tareas)
print("Posición de Estudiar:", posicion)