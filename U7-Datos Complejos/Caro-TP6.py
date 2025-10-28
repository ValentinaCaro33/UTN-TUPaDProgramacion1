#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

#Ejercicio 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

#Ejercicio 3
print(precios_frutas.values())

#Ejercicio 4
numContactos= {}

for i in range(5):
    claveContacto = str(input("Ingrese el nombre del contacto que desea agregar: "))
    valorNum = int(input("Ingrese su número telefónico correspondiente: "))
    numContactos[claveContacto]= valorNum
    
nombre= input("Ingerse un nombre para enseñarle su número: ")

if nombre in numContactos:
    print(numContactos[nombre])
else:
    print("Ese nombre no está en la lista actual de contactos.")

#Ejercicio 5
palabrasUnicas = {}

frase= input("ingrese una frase: ")

palabras = set(frase.split())
cantidad = 0

for i in palabras:
    cantidad += 1
    palabrasUnicas[i] = cantidad

print(palabras)
print(palabrasUnicas)

#Ejercicio 6
alumnos = {}

for i in range(3):
    nombre= input(f"Ingresa el nombre del estudiante {i+1}: ")

    nota1= int(input(f"Ingrese la primer nota de {nombre}: "))
    nota2= int(input(f"Ingrese la segunda nota de {nombre}: "))
    nota3= int(input(f"Ingrese la tercer nota de {nombre}: "))

    notas= (nota1, nota2, nota3)
    alumnos[nombre]= notas

for nombre, notas in alumnos.items():
    promedio= sum(notas) / len(notas)
    print(f"El promedio de {nombre} es de {promedio}")

#Ejercicio 7

parcial1= {1, 3, 8, 9, 11, 13, 14, 15}
parcial2= {1, 2, 8, 10, 12, 13, 15}

ambos= parcial1 & parcial2
print(f"Los estudiantes que aprobaron los dos parciales son: {ambos}.")

soloUno= parcial1 ^ parcial2
print(f"Los estudiantes que aprobaron solo uno de los parciales son: {soloUno}.")

alMenosUno= parcial1 | parcial2
print(f"Los estudiantes que aprobaron al menos un parcial son: {alMenosUno}.")

#Ejercicio 8
stockProductos= {"Shampoo": 15, "Jabón": 20, "Perfume": 12, "Crema": 22}

option= input("Que desea hacer: revisar el stock (r), agregar unidades (au) o agregar un nuevo producto (ap)? ")

if option == "r":
    producto = input("Ingrese el producto a consultar: ")
    if producto in stockProductos:
        print(f"Stock de {producto}: {stockProductos[producto]} unidades")
    else:
        print("Ese producto no se encuentra en el stock.")

elif option == "au":
    producto= input("Ingrese el producto al que le quiere agregar más unidades: ")
    if producto in stockProductos:
        cantidad= int(input("Ingrese la cantidad de unidades que desea agregar: "))
        stockProductos[producto] += cantidad 
    else:
        print("Ese producto no se encuentra en el stock.")
    
elif option == "ap":
    nuevo= input("Ingrese el nuevo producto que quiere agregar al stock: ")
    cantidad = int(input("Ingrese la cantidad inicial de unidades: "))
    stockProductos[nuevo] = cantidad

#Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "09:00"): "Presentación proyecto",
    ("Martes", "16:00"): "Gym",
    ("Miércoles", "11:00"): "Dentista",
    ("Viernes", "18:00"): "Salida con amigos"
}

print("Para consultar una actividad: ")
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"{dia} a las {hora} tenés: {agenda[clave]}")
else:
    print(f"No hay ninguna actividad programada para el {dia} a las {hora}.")

#Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Perú": "Lima"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(capitales_paises)