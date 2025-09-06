#Actividad 1
age= int(input("Ingrese su edad: "))

if age >= 18:
    print("Es mayor de edad.")

#Actividad 2
nota= float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#Actividad 3
num= int(input("Ingrese un número par: "))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#Actividad 4
age= int(input("Ingrese su edad: "))

if age < 12:
    print("Categoria: Niño/a")
elif age >=12 and age < 18:
    print("Categoria: Adolescente")
elif age >= 18 and age < 30:
    print("Categoria: Adulto/a joven")
elif age >= 30:
    print("Categoria: Adulto/a")

#Actividad 5
passcode= input("Ingrese una contraseña valida: ")

if len(passcode) >= 8 and len(passcode) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

if mode(numeros_aleatorios) == median(numeros_aleatorios) == mean(numeros_aleatorios):
    print("No hay sesgo.")
elif mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Hay sesgo positivo.")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Hay sesgo negativo.")

#Actividad 7
text= input("Ingrese una frase o palabra: ")
vocales= {"a","e","i","o","u"}

if text[-1] in vocales:
    print(text + "!")
else:
    print(text)

#Actividad 8
name= input("Ingrese su nombre: ")
num= int(input("Elija 1 si desea su nombre en mayusculas, 2 si desea su nombre en minusculas o 3 si desea su nombre con la primer letra en mayuscula: "))

if num == 1:
    print(name.upper())
elif num == 2:
    print(name.lower())
elif num == 3:
    print(name.title())

#Actividad 9
mag= int(input("Ingrese la magnitud del terremoto: "))

if mag < 3:
    print("Muy leve (imperceptible)")
elif mag >= 3 and mag < 4:
    print("Leve (ligeramente perceptible)")
elif mag >= 4 and mag < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif mag >= 5 and mag < 6:
    print("Fuerte (puede causar daños a estructuras débiles)")
elif mag >= 6 and mag < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif mag >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

#Actividad 10
hem= input("Ingrese en que hemisferio se encuentra: ").title()
mes= input("ingrese que mes del año es: ").title()
dia= int(input("Ingrese que dia es: "))

if mes == "Diciembre":
    if dia <= 20:
        mes = "Dic1"
    else:
        mes = "Dic2"
elif mes == "Marzo":
    if dia <= 20:
        mes = "Marz1"
    else:
        mes = "Marz2"
elif mes == "Junio":
    if dia <= 20:
        mes = "Jun1"
    else:
        mes = "Jun2"
elif mes == "Septiembre":
    if dia <= 20:
        mes = "Sep1"
    else:
        mes = "Sep2"

if hem == "Norte":
    if mes in ["Dic2", "Enero", "Febrero", "Marz1"]:
        print("Usted se encuentra en invierno.")
    elif mes in ["Marz2", "Abril", "Mayo", "Jun1"]:
        print("Usted se encuentra en primavera")
    elif mes in ["Jun2", "Julio", "Agosto", "Sep1"]:
        print("Usted se encuentra en verano")
    elif mes in ["Sep2", "Octubre", "Noviembre", "Dic1"]:
        print("Usted se encuentra en otoño")
elif hem == "Sur":
    if mes in ["Dic2", "Enero", "Febrero", "Marz1"]:
        print("Usted se encuentra en verano.")
    elif mes in ["Marz2", "Abril", "Mayo", "Jun1"]:
        print("Usted se encuentra en otoño")
    elif mes in ["Jun2", "Julio", "Agosto", "Sep1"]:
        print("Usted se encuentra en invierno")
    elif mes in ["Sep2", "Octubre", "Noviembre", "Dic1"]:
        print("Usted se encuentra en primavera")
