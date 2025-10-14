# ejercicio 1
def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo()

# ejercicio 2
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")

saludar_usuario(nombre)

# ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= int(input("Ingrese su edad: "))
residencia= input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# ejercicio 4
import math

def calcular_area_circulo(radio):
    area= math.pi * radio**2
    return print(f"el area del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro= 2 * math.pi * radio
    return print(f"el perimetro del circulo es {perimetro}")

radio= int(input("Ingrese el radio del circulo: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# ejercicio 5
def segundos_a_horas(segundos):
   horas= segundos // 3600
   return print(f"Esa cantidad de segundos son {horas} horas")

segundos= int(input("Ingrese una cantidad de segundos: "))

segundos_a_horas(segundos)

# ejercicio 6
def tabla_multiplicar(numero):
    for i in range (1,11):
        resultado= numero * i
        print(f"{numero} x {i} = {resultado}")
    
numero= int(input("Ingrese un número: "))
tabla_multiplicar(numero)

# ejercicio 7
def funciones_basicas(a,b):
    suma= a+b
    print(f"la suma de los numeros es: {suma}")
    resta= a-b
    print(f"la resta de los numeros es: {resta}")
    mult= a*b
    print(f"la multiplicación de los numeros es: {mult}")
    div= a/b
    print(f"la división de los numeros es: {div}")

a= int(input("Ingrese un número: "))
b= int(input("Ingrese otro número: "))

funciones_basicas(a, b)

# ejercicio 8
def calcular_imc(peso, altura):
    IMC= peso/(altura**2)
    return print(f"Su IMC es {IMC}")

peso= float(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su altura en m: "))

calcular_imc(peso, altura)

# ejercicio 9
def celsius_a_fahrenheit(celsius):
    f= celsius * (9/5) + 32
    return print(f"La temperatura ingresada en Fahrenheit son {f} grados.")

celsius= int(input("Ingrese una temperatura en °C: "))
celsius_a_fahrenheit(celsius)

# ejercicio 10
def  calcular_promedio(a, b, c):
    promedio= (a+b+c) / 3
    return print(f"El promedio de los numeros ingresados es: {promedio}")

a= float(input("Ingrese un número: "))
b= float(input("Ingrese otro número: "))
c= float(input("Ingrese un último número: "))

calcular_promedio(a, b, c)