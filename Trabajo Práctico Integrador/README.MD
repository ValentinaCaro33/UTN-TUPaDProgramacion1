# Gestión de Países en Python

## 📘 Descripción del Proyecto
Este proyecto forma parte del **Trabajo Práctico Integrador** de la materia **Programación 1** de la **Tecnicatura Universitaria en Programación a Distancia (UTN)**.  
El sistema implementa una **gestión de información sobre países del mundo** utilizando archivos **CSV** y operaciones **CRUD** completas.

### Objetivo General
Desarrollar un programa funcional en Python que permita:
- Agregar, consultar, actualizar y guardar información de países.
- Aplicar algoritmos de ordenamiento y filtrado.
- Calcular estadísticas descriptivas.
- Validar datos, incluyendo la verificación de países reales (193 reconocidos por la ONU).

---

## 🏛️ Universidad y Cátedra
**Universidad:** Universidad Tecnológica Nacional (UTN)  
**Carrera:** Tecnicatura Universitaria en Programación a Distancia  
**Materia:** Programación 1  

**Profesores:**
- Titular: **Alberto Cortez**  
- Comisión 3: **Brian Lara**  
- Comisión 13: **Miguel Barrera**

---

## 👥 Integrantes
- **Valentina Caro** – Comisión 3  
- **Leonardo Stamile** – Comisión 13  

**Fecha de entrega:** 11 de noviembre de 2025

---

## 🧱 Estructura del Proyecto
```
tpi_paises.py           # Script principal con todas las funciones del programa
paises.csv              # Archivo CSV con los datos (se crea o modifica automáticamente)
README.md               # Documento descriptivo del proyecto
```

El programa utiliza una estructura modular con funciones especializadas para cada operación:
- Validaciones: `texto_no_vacio()`, `es_entero_positivo()`, `pais_esta_permitido()`
- CRUD: `agregar_pais()`, `actualizar_pais()`, `buscar_por_nombre()`
- Filtrado: `filtrar_por_continente()`, `filtrar_por_rango_poblacion()`, `filtrar_por_rango_superficie()`
- Ordenamiento: `ordenar_por_nombre()`, `ordenar_por_poblacion()`, `ordenar_por_superficie()`
- Persistencia CSV: `cargar_desde_csv()`, `guardar_a_csv()`
- Estadísticas: `estadisticas()`

---

## ⚙️ Instrucciones de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/usuario/tpi_paises.git
   cd tpi_paises
   ```

2. **Ejecutar el programa:**
   ```bash
   python tpi_paises.py
   ```

3. **Interfaz de menú:**
   Al iniciar, el programa mostrará un menú interactivo con las siguientes opciones:
   ```
   1) Cargar países desde CSV
   2) Guardar países a CSV
   3) Agregar país
   4) Actualizar población y superficie
   5) Buscar país por nombre
   6) Filtrar por continente
   7) Filtrar por rango de población
   8) Filtrar por rango de superficie
   9) Ordenar por nombre
   10) Ordenar por población
   11) Ordenar por superficie
   12) Mostrar estadísticas
   0) Salir
   ```

---

## 🎥 Enlaces
- **Video explicativo:** [🔗 Enlace al video](https://youtu.be/CKHOuVgVxBQ?si=P1lqfzrKfjqCsUiD)
- **Repositorio GitHub:** [🔗 Enlace al repositorio](https://github.com/ValentinaCaro33/UTN-TUPaDProgramacion1/tree/1cee0877c8336a7668efca7dab699a3942702c1d/Trabajo%20Pr%C3%A1ctico%20Integrador)


---

## 💻 Ejemplo de Entrada y Salida

### Ejemplo de entrada (al agregar países)
```
Nombre: Argentina
Población: 45376763
Superficie: 2780400
Continente: América
```

### Ejemplo de salida
```
País agregado correctamente.
```

### Ejemplo de filtrado
```
Opción: 6
Continente: Europa
```

**Salida:**
```
Nombre: Alemania | Población: 83149300 | Superficie: 357022 | Continente: Europa
Nombre: Italia | Población: 59550000 | Superficie: 301340 | Continente: Europa
Nombre: Suiza | Población: 8717000 | Superficie: 41285 | Continente: Europa
```

---

## 📊 Ejemplo de Estadísticas
```
País con mayor población: Brasil (213993437)
País con menor población: Suiza (8717000)
Promedio de población: 86,234,828.57
Promedio de superficie: 2,335,057.0
Cantidad de países por continente:
  - América: 2
  - Europa: 3
  - Asia: 1
```

---

## 🧩 Tecnologías Utilizadas
- **Lenguaje:** Python 3.10+
- **Formato de datos:** CSV
- **Paradigma:** Programación estructurada y modular
- **Bibliotecas estándar:** `os`

---

## 🧾 Licencia
Este proyecto fue desarrollado con fines académicos para la UTN y no posee licencia de distribución comercial.