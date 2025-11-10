# TPI Programacion 1 - Gestion de Datos de Paises

# Modelo de datos
# valida que el texto no este vacio

# Validaciones simples

def texto_no_vacio(s):
    s = str(s).strip()
    if s == "":
        return False
    return True


def es_entero_positivo(cadena): # valida que un valor sea un numero entero positivo. Acepta solo digitos (sin signos ni puntos).
    if not texto_no_vacio(cadena):
        return False
    for ch in cadena.strip():
        if ch < '0' or ch > '9':
            return False
    return True

# lista completa de paises permitidos (Reconocidos por ONU)
PAISES_PERMITIDOS = [
    "afganistan", "albania", "alemania", "andorra", "angola", "antigua y barbuda",
    "arabia saudita", "argelia", "argentina", "armenia", "australia", "austria", "azerbaiyan",
    "bahamas", "banglades", "barbados", "barein", "belgica", "belice", "benin",
    "bielorrusia", "birmania", "bolivia", "bosnia y herzegovina", "botsuana", "brasil",
    "brunei", "bulgaria", "burkina faso", "burundi", "cabo verde", "camboya", "camerun",
    "canada", "catar", "chad", "chile", "china", "chipre", "colombia", "comoras",
    "corea del norte", "corea del sur", "costa de marfil", "costa rica", "croacia", "cuba",
    "dinamarca", "dominica", "ecuador", "egipto", "el salvador", "emiratos arabes unidos",
    "eritrea", "eslovaquia", "eslovenia", "espana", "estados unidos", "estonia",
    "esuatini", "etiopia", "filipinas", "finlandia", "fiyi", "francia", "gabon", "gambia",
    "georgia", "ghana", "granada", "grecia", "guatemala", "guinea", "guinea-bisau",
    "guinea ecuatorial", "guyana", "haiti", "honduras", "hungria", "india", "indonesia",
    "irak", "iran", "irlanda", "islandia", "islas marshall", "islas salomon", "israel",
    "italia", "jamaica", "japon", "jordania", "kazajistan", "kenia", "kirguistan", "kiribati",
    "kuwait", "laos", "lesoto", "letonia", "libano", "liberia", "libia", "liechtenstein",
    "lituania", "luxemburgo", "madagascar", "malasia", "malaui", "maldivas", "mali",
    "malta", "marruecos", "mauricio", "mauritania", "mexico", "micronesia", "moldavia",
    "monaco", "mongolia", "montenegro", "mozambique", "namibia", "nauru", "nepal",
    "nicaragua", "niger", "nigeria", "noruega", "nueva zelanda", "oman", "paises bajos",
    "pakistan", "palaos", "panama", "papua nueva guinea", "paraguay", "peru", "polonia",
    "portugal", "reino unido", "republica centroafricana", "republica checa",
    "republica del congo", "republica democratica del congo", "republica dominicana",
    "ruanda", "rumania", "rusia", "samoa", "san cristobal y nieves", "san marino",
    "san vicente y las granadinas", "santa lucia", "santo tome y principe", "senegal",
    "serbia", "seychelles", "sierra leona", "singapur", "siria", "somalia", "sri lanka",
    "sudafrica", "sudan", "sudan del sur", "suecia", "suiza", "surinam", "tailandia",
    "tanzania", "tayikistan", "timor oriental", "togo", "tonga", "trinidad y tobago",
    "tunez", "turkmenistan", "turquia", "tuvalu", "ucrania", "uganda", "uruguay",
    "uzbekistan", "vanuatu", "venezuela", "vietnam", "yemen", "zambia", "zimbabue"
]

def pais_esta_permitido(nombre):
    if not texto_no_vacio(nombre):
        return False
    n = nombre.strip().lower()
    i = 0
    while i < len(PAISES_PERMITIDOS):
        if PAISES_PERMITIDOS[i] == n:
            return True
        i = i + 1
    return False


# muestra el menu principal en pantalla


# CSV: cargar y guardar

def cargar_desde_csv(ruta): # carga la lista de paises desde el archivo CSV
    lista = []
    import os
    if not os.path.exists(ruta):
        return lista, "No se pudo abrir el archivo CSV. Se continuara con la lista vacia."
    
    f = open(ruta, "r", encoding="utf-8")
    lineas = f.readlines()
    f.close()

    # Se espera encabezado: nombre,poblacion,superficie,continente
    if len(lineas) == 0:
        return lista, "El CSV esta vacio. Se continuara con la lista vacia."

    # Procesa filas
    encabezado = True
    for linea in lineas:
        linea = linea.strip() # ignora lineas vacias o con formato incorrecto
        if linea == "":
            continue # evita duplicar paises con el mismo nombre
        if encabezado:
            encabezado = False
            continue  # saltamos el header

        partes = linea.split(",")
        if len(partes) != 4: # Linea invalida, se ignora
            continue

        nombre = partes[0].strip()
        poblacion_txt = partes[1].strip()
        superficie_txt = partes[2].strip()
        continente = partes[3].strip()

        if not (texto_no_vacio(nombre) and texto_no_vacio(continente)):  # Datos de texto invalidos
            continue

        if not (es_entero_positivo(poblacion_txt) and es_entero_positivo(superficie_txt)):
            continue

        pais = {
            "nombre": nombre,
            "poblacion": int(poblacion_txt),
            "superficie": int(superficie_txt),
            "continente": continente
        }
        lista.append(pais)

    return lista, "CSV cargado correctamente."


def guardar_a_csv(ruta, lista_paises): # guarda la lista actual de paises al archivo CSV
    import os
    directorio = os.path.dirname(ruta)
    if directorio != "" and not os.path.exists(directorio):
        return False, "No se pudo guardar el archivo CSV."
    
    f = open(ruta, "w", encoding="utf-8")
    f.write("nombre,poblacion,superficie,continente\n")
    i = 0
    while i < len(lista_paises):
        p = lista_paises[i]
        fila = p["nombre"] + "," + str(p["poblacion"]) + "," + str(p["superficie"]) + "," + p["continente"]
        f.write(fila + "\n")
        i = i + 1
    f.close()
    return True, "CSV guardado correctamente."


# Altas, busquedas y actualizaciones
# agrega un nuevo pais a la lista si los datos son validos

def agregar_pais(lista_paises, nombre, poblacion_txt, superficie_txt, continente):
    if not texto_no_vacio(nombre):
        return False, "El nombre no puede estar vacio."
    if not pais_esta_permitido(nombre):   # <- ESTA LINEA TIENE QUE ESTAR
        return False, "Ese pais no esta en la lista permitida."
    if not texto_no_vacio(continente):
        return False, "El continente no puede estar vacio."
    if not es_entero_positivo(poblacion_txt):
        return False, "La poblacion debe ser un entero positivo."
    if not es_entero_positivo(superficie_txt):
        return False, "La superficie debe ser un entero positivo."

    # Evitar duplicados por nombre exacto
    i = 0
    while i < len(lista_paises):
        if lista_paises[i]["nombre"].lower() == nombre.strip().lower():
            return False, "Ya existe un pais con ese nombre."
        i = i + 1

    pais = {
        "nombre": nombre.strip(),
        "poblacion": int(poblacion_txt.strip()), # calcula estadisticas generales de la lista de paises
        "superficie": int(superficie_txt.strip()),
        "continente": continente.strip()
    }
    lista_paises.append(pais)
    return True, "Pais agregado correctamente."


# busca paises por nombre (coincidencia parcial o exacta)
def buscar_por_nombre(lista_paises, texto_busqueda):    # Coincidencia parcial y exacta (insensible a mayusculas/minusculas)
    resultados = []
    if not texto_no_vacio(texto_busqueda):
        return resultados
    t = texto_busqueda.strip().lower()
    i = 0
    while i < len(lista_paises):
        nombre = lista_paises[i]["nombre"].lower()
        if t in nombre:
            resultados.append(lista_paises[i])
        i = i + 1
    return resultados


def actualizar_pais(lista_paises, nombre_busqueda, nueva_poblacion_txt, nueva_superficie_txt):
    if not texto_no_vacio(nombre_busqueda):
        return False, "Debe indicar el nombre del pais a actualizar."
    if not es_entero_positivo(nueva_poblacion_txt):
        return False, "La poblacion debe ser un entero positivo."
    if not es_entero_positivo(nueva_superficie_txt):
        return False, "La superficie debe ser un entero positivo."

    nombre_busqueda = nombre_busqueda.strip().lower()
    i = 0
    while i < len(lista_paises):
        if lista_paises[i]["nombre"].lower() == nombre_busqueda:
            lista_paises[i]["poblacion"] = int(nueva_poblacion_txt.strip())
            lista_paises[i]["superficie"] = int(nueva_superficie_txt.strip())
            return True, "Pais actualizado correctamente."
        i = i + 1
    return False, "No se encontro un pais con ese nombre (busqueda exacta)."


# Filtros

# filtra paises segun el continente indicado
def filtrar_por_continente(lista_paises, continente):
    res = []
    if not texto_no_vacio(continente):
        return res
    c = continente.strip().lower()
    i = 0
    while i < len(lista_paises):
        if lista_paises[i]["continente"].strip().lower() == c:
            res.append(lista_paises[i])
        i = i + 1
    return res


# filtra paises segun rango de poblacion
def filtrar_por_rango_poblacion(lista_paises, minimo_txt, maximo_txt):
    res = []
    if not es_entero_positivo(minimo_txt):
        return res
    if not es_entero_positivo(maximo_txt):
        return res
    minimo = int(minimo_txt.strip())
    maximo = int(maximo_txt.strip())
    if minimo > maximo: # Intercambiar
        temp = minimo
        minimo = maximo
        maximo = temp

    i = 0
    while i < len(lista_paises):
        p = lista_paises[i]["poblacion"]
        if p >= minimo and p <= maximo:
            res.append(lista_paises[i])
        i = i + 1
    return res


# filtra paises segun rango de superficie
def filtrar_por_rango_superficie(lista_paises, minimo_txt, maximo_txt):
    res = []
    if not es_entero_positivo(minimo_txt):
        return res
    if not es_entero_positivo(maximo_txt):
        return res
    minimo = int(minimo_txt.strip())
    maximo = int(maximo_txt.strip())
    if minimo > maximo:
        temp = minimo
        minimo = maximo
        maximo = temp

    i = 0
    while i < len(lista_paises):
        s = lista_paises[i]["superficie"]
        if s >= minimo and s <= maximo:
            res.append(lista_paises[i])
        i = i + 1
    return res

# Ordenamientos

def ordenar_por_nombre(lista_paises): # Retorna una nueva lista ordenada ascendente por nombre
    copia = copiar_lista_paises(lista_paises)
    n = len(copia)
    i = 0
    while i < n:
        j = 0
        while j < n - 1 - i:
            if copia[j]["nombre"].lower() > copia[j + 1]["nombre"].lower():
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
            j = j + 1
        i = i + 1
    return copia


def ordenar_por_poblacion(lista_paises, ascendente=True):
    copia = copiar_lista_paises(lista_paises)
    n = len(copia)
    i = 0
    while i < n:
        j = 0
        while j < n - 1 - i:
            a = copia[j]["poblacion"]
            b = copia[j + 1]["poblacion"]
            condicion = (a > b) if ascendente else (a < b)
            if condicion:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
            j = j + 1
        i = i + 1
    return copia


def ordenar_por_superficie(lista_paises, ascendente=True):
    copia = copiar_lista_paises(lista_paises)
    n = len(copia)
    i = 0
    while i < n:
        j = 0
        while j < n - 1 - i:
            a = copia[j]["superficie"]
            b = copia[j + 1]["superficie"]
            condicion = (a > b) if ascendente else (a < b)
            if condicion:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
            j = j + 1
        i = i + 1
    return copia


def copiar_lista_paises(lista_paises): # Copia de lista de diccionarios
    copia = []
    i = 0
    while i < len(lista_paises):
        p = lista_paises[i]
        nuevo = {
            "nombre": p["nombre"],
            "poblacion": p["poblacion"],
            "superficie": p["superficie"],
            "continente": p["continente"]
        }
        copia.append(nuevo)
        i = i + 1
    return copia

# Estadisticas

def estadisticas(lista_paises): # Devuelve un diccionario con:'mayor_poblacion' (pais), 'menor_poblacion' (pais),'promedio_poblacion' (float), 'promedio_superficie' (float),'cantidad_por_continente' (dict)
    res = {
        "mayor_poblacion": "",
        "menor_poblacion": "",
        "promedio_poblacion": 0.0,
        "promedio_superficie": 0.0,
        "cantidad_por_continente": {}
    }
    if len(lista_paises) == 0:
        return res

    # Mayor y menor poblacion
    mayor = lista_paises[0]
    menor = lista_paises[0]
    suma_poblacion = 0
    suma_superficie = 0

    i = 0
    while i < len(lista_paises):
        p = lista_paises[i]
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
        if p["poblacion"] < menor["poblacion"]:
            menor = p
        suma_poblacion = suma_poblacion + p["poblacion"]
        suma_superficie = suma_superficie + p["superficie"]
        i = i + 1

    promedio_p = suma_poblacion / len(lista_paises)
    promedio_s = suma_superficie / len(lista_paises)

    # Cantidad por continente
    conteo = {}
    i = 0
    while i < len(lista_paises):
        c = lista_paises[i]["continente"]
        if c in conteo:
            conteo[c] = conteo[c] + 1
        else:
            conteo[c] = 1
        i = i + 1

    res["mayor_poblacion"] = mayor
    res["menor_poblacion"] = menor
    res["promedio_poblacion"] = promedio_p
    res["promedio_superficie"] = promedio_s
    res["cantidad_por_continente"] = conteo
    return res

# Utilidades de impresion (devuelven texto)

def formatear_pais(p):
    return ("Nombre: " + p["nombre"] +
            " | Poblacion: " + str(p["poblacion"]) +
            " | Superficie: " + str(p["superficie"]) +
            " | Continente: " + p["continente"])


def formatear_lista_paises(lista):
    if len(lista) == 0:
        return "Sin resultados."
    i = 0
    texto = ""
    while i < len(lista):
        texto = texto + formatear_pais(lista[i]) + "\n"
        i = i + 1
    return texto


def formatear_estadisticas(est):
    texto = ""
    if est["mayor_poblacion"] != "":
        texto = texto + "Pais con mayor poblacion: " + formatear_pais(est["mayor_poblacion"]) + "\n"
    if est["menor_poblacion"] != "":
        texto = texto + "Pais con menor poblacion: " + formatear_pais(est["menor_poblacion"]) + "\n"
    texto = texto + "Promedio de poblacion: " + str(est["promedio_poblacion"]) + "\n"
    texto = texto + "Promedio de superficie: " + str(est["promedio_superficie"]) + "\n"
    texto = texto + "Cantidad de paises por continente:\n"
    for cont in est["cantidad_por_continente"]:
        texto = texto + "  - " + cont + ": " + str(est["cantidad_por_continente"][cont]) + "\n"
    return texto

# Menu (flujo principal)

def menu():
    print("====================================")
    print("   Gestion de Datos de Paises (CSV) ")
    print("====================================")
    print("1) Cargar paises desde CSV")
    print("2) Guardar paises a CSV")
    print("3) Agregar pais")
    print("4) Actualizar poblacion y superficie de un pais (por nombre exacto)")
    print("5) Buscar pais por nombre (parcial)")
    print("6) Filtrar por continente")
    print("7) Filtrar por rango de poblacion")
    print("8) Filtrar por rango de superficie")
    print("9) Ordenar por nombre (A-Z)")
    print("10) Ordenar por poblacion (ascendente)")
    print("11) Ordenar por superficie (elige asc/desc)")
    print("12) Mostrar estadisticas")
    print("0) Salir")


def pedir_opcion():
    op = input("Elegi una opcion: ").strip()
    return op


def main():
    lista_paises = []
    ruta_csv = "paises.csv"  

    # Ejemplos tomados de la consigna mas agregados por nuestro grupo
    # nombre,poblacion,superficie,continente
    # Argentina,45376763,2780400,America
    # Japon,125800000,377975,Asia
    # Brasil,213993437,8515767,America
    # Alemania,83149300,357022,Europa
    # Inglaterra,56000000,243610,Europa
    # Suiza,8717000,41285,Europa
    # Italia,59550000,301340,Europa

    salir = False
    while not salir:
        menu()
        opcion = pedir_opcion()

        if opcion == "1":
            lista_paises, msj = cargar_desde_csv(ruta_csv)
            print(msj)

        elif opcion == "2":
            exito, msj = guardar_a_csv(ruta_csv, lista_paises)
            print(msj)

        elif opcion == "3":
            nombre = input("Nombre: ")  # valida apenas se ingresa el nombre
            if not pais_esta_permitido(nombre):
                print("Ese pais no esta permitido o es inexistente.")
                print("")  # separador visual
            else:
                poblacion = input("Poblacion (entero positivo): ")
                superficie = input("Superficie en km2 (entero positivo): ")
                continente = input("Continente: ")
                exito, msj = agregar_pais(lista_paises, nombre, poblacion, superficie, continente)
                print(msj)

        elif opcion == "4":
            nombre = input("Nombre EXACTO del pais a actualizar: ").strip()
            nueva_pob = input("Nueva poblacion: ").strip()
            nueva_sup = input("Nueva superficie: ").strip()
            exito, msj = actualizar_pais(lista_paises, nombre, nueva_pob, nueva_sup)
            print(msj)

        elif opcion == "5":
            texto = input("Texto de busqueda (parcial o exacto): ")
            resultados = buscar_por_nombre(lista_paises, texto)
            print(formatear_lista_paises(resultados))

        elif opcion == "6":
            cont = input("Continente (ej: America, Europa, Asia, Africa, Oceania): ")
            resultados = filtrar_por_continente(lista_paises, cont)
            print(formatear_lista_paises(resultados))

        elif opcion == "7":
            minimo = input("Poblacion minima: ")
            maximo = input("Poblacion maxima: ")
            resultados = filtrar_por_rango_poblacion(lista_paises, minimo, maximo)
            print(formatear_lista_paises(resultados))

        elif opcion == "8":
            minimo = input("Superficie minima: ")
            maximo = input("Superficie maxima: ")
            resultados = filtrar_por_rango_superficie(lista_paises, minimo, maximo)
            print(formatear_lista_paises(resultados))

        elif opcion == "9":
            ordenados = ordenar_por_nombre(lista_paises)
            print(formatear_lista_paises(ordenados))

        elif opcion == "10":
            ordenados = ordenar_por_poblacion(lista_paises, True)
            print(formatear_lista_paises(ordenados))

        elif opcion == "11":
            tipo = input("Elegi tipo (asc/desc): ").strip().lower()
            asc = True
            if tipo == "desc":
                asc = False
            ordenados = ordenar_por_superficie(lista_paises, asc)
            print(formatear_lista_paises(ordenados))

        elif opcion == "12":
            est = estadisticas(lista_paises)
            print(formatear_estadisticas(est))

        elif opcion == "0":
            salir = True
            print("Saliendo...")
        else:
            print("Opcion invalida.")

        print("")  # Separador visual

if __name__ == "__main__":
    main()
