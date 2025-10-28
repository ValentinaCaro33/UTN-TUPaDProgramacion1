with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120,30\n")
    archivo.write("Cartuchera,200,25\n")
    archivo.write("Marcador,150,32\n")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")
        print(f"Producto: {datos[0]} | Precio: ${datos[1]} | Cantidad: {datos[2]}")

producto= input("Ingrese un nuevo producto: ")
precio= input("Ingrese su precio: ")
cant= input("Ingrese su cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{producto},{precio},{cant}\n")

productos= []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")
        producto = {
            'nombre': datos[0],
            'precio': datos[1],
            'cantidad': datos[2]
        }
        productos.append(producto)

print("\n productos en la lista")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado= False

for p in productos:
    if buscar in p['nombre']:
        print(f"Producto encontrado:")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado= True
        break

if not encontrado:
        print("Producto no encontrado")

with open('productos.txt', 'w') as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
