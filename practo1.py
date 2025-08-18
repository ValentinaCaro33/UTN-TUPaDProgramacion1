#Ejercicio1
print("Hola Mundo!")

#Ejercicio2
name= input("Ingrese su nombre: ")

print(f"Hola {name}!")

#Ejercicio3
name= input("Ingrese su nombre: ")
surname= input("Ingrese su apellido: ")
age= input("Ingrese su edad: ")
home= input("Ingrese donde vive: ")

print(f"Soy {name} {surname}, tengo {age} años y vivo en {home}")

#Ejercicio4
r= float(input("Ingrese el radio de un circulo: "))

a= 3.14 * r**2
p= 2*3.14*r

print(f"El área del circulo es de {a} y su perímetro es de {p}.")

#Ejercicio5
seg= float(input("Ingrese una cantidad de segundos: "))

horas= seg/3600

print(f"La cantidad de segundos ingresados equivalen a {horas} horas.")

#Ejercicio6
num= float(input("Ingrese un numero: "))

print(f"La tabla de multiplicar de {num} es: ")
for i in range (1,11):
    resultado= num*i
    print(f"{num} x {i}= {resultado}")

#Ejercicio7
num1= float(input("Ingrese un numero entero: "))
if num1==0:
    num1= float(input("El numero debe ser distinto a 0, intente de nuevo: "))
num2= float(input("Ingrese otro numero entero: "))
if num2==0:
    num2= float(input("El numero debe ser distinto a 0, intente de nuevo: "))

suma= num1+num2
print(f"la suma de los numeros es: {suma}")
resta= num1-num2
print(f"la resta de los numeros es: {resta}")
mult= num1*num2
print(f"la multiplicación de los numeros es: {mult}")
div= num1/num2
print(f"la división de los numeros es: {div}")

#Ejercicio8
altura= float(input("Ingrese su altura en m: "))
peso= float(input("Ingrese su peso en kg: "))

IMC= peso/altura**2

print(f"Su IMC es {IMC}")

#Ejercicio9
cel= float(input("Ingrese una temperatura en °C: "))

f= cel * (9/5) + 32

print(f"La temperatura ingresada en Fahrenheit son {f} grados.")

#Ejercicio10
num1= float(input("Ingrese un número: "))

num2= float(input("Ingrese otro número: "))

num3= float(input("Ingrese un último número: "))

prom= (num1+num2+num3) / 3

print(f"El promedio de los numeros ingresados es: {prom}")