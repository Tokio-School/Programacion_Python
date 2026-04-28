pedidos = [
    "PED001:raton,teclado,pantalla",
    "PED002:portatil,raton",
    "PED003:teclado,webcam,raton"
]

productos_totales = []

for pedido in pedidos:
    partes = pedido.split(":")
    codigo = partes[0]
    productos = partes[1].split(",")

    for producto in productos:
        producto = producto.replace("raton", "mouse")
        productos_totales.append(producto)

cantidad_mouse = productos_totales.count("mouse")

productos_totales.sort()

resumen = " | ".join(productos_totales)

print("Productos ordenados:", productos_totales)
print("Cantidad de mouse:", cantidad_mouse)
print("Resumen:", resumen)