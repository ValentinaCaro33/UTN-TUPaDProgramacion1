# EJercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):
    print(f"Factorial de {i}: {factorial(i)}")

# EJercicio 2
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición: "))
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")

# EJercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

n = int(input("Ingrese la base: "))
m = int(input("Ingrese el exponente: "))
print(f"{n}^{m} = {potencia(n, m)}")

# EJercicio 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal: "))
if numero == 0:
    print("0")
else:
    print(decimal_a_binario(numero))

# EJercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ")
print(es_palindromo(texto))

# EJercicio 6
def suma_digitos(n):
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número: "))
print(suma_digitos(numero))

# EJercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(contar_bloques(nivel))

# EJercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)

num = int(input("Ingrese un número: "))
dig = int(input("Ingrese el dígito a contar: "))
print(contar_digito(num, dig))