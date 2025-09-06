#Actividad 1
for i in range(0, 101):
    print(i)

#Actividad 2
num= input("Ingrese un número entero: ") 

cont= 0 

while cont <= len(num) - 1: 
    cont += 1 
    
print("la cantidad de digitos en tu número son: ", cont)

#Actividad 3
num1= int(input("Ingrese un número entero: "))
num2= int(input("Ingrese otro número entero: "))

suma=0

if num1 > num2:
    num_min= num2
    num_max= num1
else:
    num_min= num1
    num_max=num2

for i in range(num_min +1, num_max):
    suma += i

print("La suma de los numeros comprendidos en los que se ingresaron es:", suma)

#Actcividad 4:
num= int(input("Ingrese un numero, 0 para terminar: "))
suma= 0

while num != 0:
    suma += num
    num= int(input("Ingrese otro numero, 0 para terminar: "))

print("La suma de los números ingresados es: ", suma)

#Actividad 5
import random
num_aleatorio = random.randint(0, 9) 

guess= int(input("Adivina el número que estoy pensando: "))
cont=1

while guess != num_aleatorio:
    cont += 1
    guess= int(input("intenta nuevamente: "))

print("Has adivinado! te tomó ", cont, "intentos.")

#Actividad 6
for i in range(100, -2, -2):
    print(i)

#Actividad 7
num= int(input("ingrese un numero positivo: "))
suma=0

while num <= 0:
    num= int(input("No es válido, intente de nuevo: "))

for i in range(num+1):
    suma += i

print("La suma entre 0 y ", num, "es ", suma)

#Actividad 8
cant=0
num_neg=0
num_pos=0
num_par=0
num_imp=0

while cant < 100:
    num= int(input("Ingrese un numero: "))
    cant += 1

    if num > 0:
        num_pos += 1
    else:
        num_neg += 1

    if num % 2 == 0:
            num_par += 1
    else:
            num_imp += 1

print("La cantidad de numeros par son: ", num_par)
print("La cantidad de numeros impar son: ", num_imp)
print("La cantidad de numeros positivos son: ", num_pos)
print("La cantidad de numeros negativos son: ", num_neg)

#Actividad 9
suma=0
cant=0

while cant < 100:
     num= int(input("Ingrese un numero: "))
     cant += 1
     suma += num

media= suma / cant

print("La media de los numeros ingresados es: ", media)

#Actividad 10
num = input("Ingrese un número de varios dígitos: ")

num_invertido = ""
for digito in num:
    num_invertido = digito + num_invertido 

print("Número invertido:", num_invertido)