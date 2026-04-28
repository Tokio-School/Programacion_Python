etiquetas = [
    "ROPA:camiseta, pantalon, abrigo",
    "TECNOLOGIA:raton, teclado, pantalla",
    "ROPA:zapatos, gorra"
]

productos_ropa = []

for etiqueta in etiquetas:
    partes = etiqueta.split(":")
    categoria = partes[0]
    productos = partes[1].split(",")

    if categoria == "ROPA":
        for producto in productos:
            producto = producto.replace(" ", "")
            productos_ropa.append(producto)

productos_ropa.insert(0, "bufanda")

if "gorra" in productos_ropa:
    productos_ropa.remove("gorra")

productos_ropa.sort()
productos_ropa.reverse()

resultado = ", ".join(productos_ropa)

print("Productos de ropa:", resultado)