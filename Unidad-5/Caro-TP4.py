#Actividad 1
notas= [10, 8, 5, 6, 7, 4, 9, 9, 6, 3]

i=0
suma=0
nota_max= notas[0]
nota_min= notas[0]

for i in range(len(notas)):
    print(notas[i])

for i in range (len(notas)):
    suma += notas[i]
    
promedio = suma/len(notas)

print(f"el promedio de las notas es {promedio}")

for i in range (1, len(notas)):
    if notas[i] > nota_max:
        nota_max= notas[i]
    elif notas[i] < nota_min:
        nota_min= notas[1]

print(f"la nota mínima es {nota_min}")
print(f"la nota máxima es {nota_max}")

#Actividad 2
lista= []

for i in range(5):
   producto= input("Ingrese productos para su lista: ")
   lista.append(producto)

lista_ordenada= sorted(lista)

print("Lista ordenada alfabeticamente:")
for i in range(len(lista)):
    print(lista_ordenada[i])

pregunta= input("Desea eliminar algun producto de su lista? ").title()

if pregunta == "Si":
    producto_2= input("Ingrese el producto que desea eliminar: ")
    if producto_2 in lista:
        lista.remove(producto_2)
        lista_ordenada= sorted(lista)
        print("Su lista actualizada es:")
        for i in range(len(lista_ordenada)):
            print(lista_ordenada[i])
elif pregunta == "No":
    print(f"su lista es: ")
    for i in range(len(lista_ordenada)):
            print(lista_ordenada[i])

#Actividad 3
import random

lista= []
num_par= []
num_impar= []

for i in range(15):
    num= (random.randint(1,100))
    lista.append(num)
    if num % 2 == 0:
        num_par.append(num)
    else:
        num_impar.append(num)

print(f"La cantidad de números pares son: {len(num_par)}")    
print(f"La cantidad de números impares son: {len(num_impar)}")

#Actividad 4
datos= [1,3,5,3,7,1,9,5,3,]
print(datos)
lista= []

for i in range (len(datos)):
    if datos[i] not in lista:
        lista.append(datos[i])

print(lista)

#Actividad 5
alumnos= ["Sebastian", "Laura", "Marta", "Esperanza", "Roberto", "Leonarda", "Angustia", "Soledad"]

print("Esta es su lista de alumnos actual: ")
for i in range(len(alumnos)):
    print(alumnos[i])

cambio= input("Desea hacer algun cambio en la lista? (si/no): ").title()

if cambio == "Si":
    cambio_1= input("Desea eliminar o agregar un nombre? (eliminar/agregar): ").title()
    if cambio_1== "Agregar":
        name= input("Ingrese el nombre a agregar: ").title()
        alumnos.append(name)
        for i in range (len(alumnos)):
            print(alumnos[i])
    elif cambio_1 == "Eliminar":
        name_1= input("Ingrese el nombre que desea eliminar: ").title()
        if name_1 in alumnos:
            alumnos.remove(name_1)
            for i in range(len(alumnos)):
                print(alumnos[i])
elif cambio == "No":
    print("Lista completada.")

#Actividad 6
numeros = [1, 2, 3, 4, 5, 6, 7]

print("Lista original:")
for i in range(len(numeros)):
    print(numeros[i])

ultimo = numeros[len(numeros)-1]  

for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1] 

numeros[0] = ultimo

print("Lista rotada hacia la derecha:")
for i in range(len(numeros)):
    print(numeros[i])

#Actividad 7
temperaturas = [
    [15, 28], 
    [12, 25], 
    [18, 32],  
    [16, 29],  
    [14, 26], 
    [20, 35], 
    [17, 30]  
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(len(temperaturas)):
    min_temp = temperaturas[i][0]
    max_temp = temperaturas[i][1]
    print(f"{dias_semana[i]}: Minima= {min_temp}° Maxima= {max_temp}°")

suma_min = 0
suma_max = 0

for i in temperaturas:
    suma_min += i[0] 
    suma_max += i[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"Promedio de temperaturas mínimas: {promedio_min}°")
print(f"Promedio de temperaturas máximas: {promedio_max}°")

mayor_amp = 0
dia_mayor = 0

for i in range(len(temperaturas)):
    amp_actual = temperaturas[i][1] - temperaturas[i][0]
    if amp_actual > mayor_amp:
        mayor_amp = amp_actual
        dia_mayor = i

print(f"El día {dias_semana[dia_mayor]} tuvo mayor amplitud con: {mayor_amp}°")

#Actividad 8
materias = ["Lengua", "Matemática", "Química"]
estudiantes = ["Leonel", "María", "Pedro", "Esteban", "Franco"]

notas = [[0]*len(materias) for _ in range(len(estudiantes))]

for i in range(len(estudiantes)):
    print(f"Ingresar notas de {estudiantes[i]}")
    for j in range(len(materias)):
        nota = float(input(f"Nota en {materias[j]}: "))
        notas[i][j] = nota

print("Promedio de estudiantes:")
for i in range(len(estudiantes)):
    promedio = sum(notas[i]) / len(notas[i])
    print(f"{estudiantes[i]}: {promedio}")

print("Promedio de materias:")
for j in range(len(materias)):
    suma = 0
    for i in range(len(estudiantes)):
        suma += notas[i][j]
    promedio = suma / len(estudiantes)
    print(f"{materias[j]}: {promedio}")

# Actividad 9
tablero = [
    ["-", "-", "-"], 
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador = "X"
jugadas = 0  

while True:
    print("Tablero de Ta-Te-Ti: ")
    for i in range(len(tablero)):
        fila_completa = ""  
        for j in range(len(tablero[i])):
            fila_completa += tablero[i][j] + " "
        print(fila_completa)

    try:
        f = int(input(f"Jugador {jugador} - Elija una fila (0, 1 o 2): "))
        c = int(input(f"Jugador {jugador} - Elija una columna (0, 1 o 2): "))

        if f not in [0,1,2] or c not in [0,1,2]:
            print("Posición inválida. Intenta nuevamente.")
            continue

        if tablero[f][c] == "-":
            tablero[f][c] = jugador
            jugadas += 1
            jugador = "O" if jugador == "X" else "X"

            print("Tablero actualizado:")
            for i in range(len(tablero)):
                print(" ".join(tablero[i]))

            if jugadas >= 5: 
                print("Fin de la demostración")
                break 

        else:
            print("Casilla ocupada")

    except ValueError:
        print("Debes ingresar un número entre 0 y 2.")

#Actividad 10
ventas = [[0]*7 for _ in range(4)]

for d in range(7): 
    print(f"Día {d+1}")
    for p in range(4):  
        valor = int(input(f"Ingrese ventas del Producto {p+1}: "))
        ventas[p][d] = valor

print("Total vendido por cada producto:")
for p in range(len(ventas)):
    total_producto = sum(ventas[p])
    print(f"Producto {p+1}: {total_producto}")

totales_dias = []
for d in range(7):
    total_dia = 0
    for p in range(4):
        total_dia += ventas[p][d]
    totales_dias.append(total_dia)

dia_max = max(totales_dias)
indice_dia = totales_dias.index(dia_max)
print(f"Día con mayores ventas totales: Día {indice_dia+1} con {dia_max} ventas")

totales_productos = [sum(fila) for fila in ventas]
max_producto = max(totales_productos)
indice_producto = totales_productos.index(max_producto)
print(f"Producto más vendido en la semana: Producto {indice_producto+1} con {max_producto} ventas")



