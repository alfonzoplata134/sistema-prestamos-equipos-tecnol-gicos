# 💻 Sistema de Gestión de Estudiantes y Equipos Tecnológicos

¡Hola! 👋 Este es un proyecto desarrollado en equipo para la gestión y control de estudiantes y recursos tecnológicos (portátiles, proyectores, tablets, etc.) desarrollado en **Python**.

Fue creado colaborativamente para aplicar conceptos fundamentales de programación: funciones, modularidad, listas, diccionarios, validaciones estrictas y almacenamiento de datos en archivos JSON.

---

## 🚀 Funcionalidades Actuales

- [x] **Gestión y Validación de Estudiantes:**
  - **Validación de Documento:** Solo números (sin letras, sin espacios) y con una longitud válida de **6 a 10 dígitos**.
  - **Normalización de Nombres:** Limpia espacios extra y guarda los nombres en formato adecuado (`.title()`), permitiendo búsquedas sin importar mayúsculas o minúsculas.
  - **Validación de Correo:** Comprobación de formato básico (`@`, `.`, sin espacios).
  - **Búsqueda Flexible:** Búsqueda tanto por número de documento como por nombre del estudiante.
  - **Listado Formateado:** Visualización en tabla limpia en la consola.
- [x] **Inventario de Equipos:**
  - Registro de dispositivos por ID (en mayúsculas), tipo, marca, modelo y estado inicial.
  - Prevención de IDs duplicados y validación de campos.
- [x] **Persistencia en JSON:**
  - Los datos se guardan en la carpeta `datos/` para no perder la información al cerrar el programa.

---

## 📁 Estructura del Proyecto

Organizamos el código de forma modular en archivos separados para trabajar en equipo de manera más sencilla:

```text
sistema-prestamos-equipos-tecnol-gicos/
│
├── datos/                  # Carpeta donde se guardan los archivos JSON
│   ├── estudiantes.json    # Datos de estudiantes guardados
│   └── equipos.json        # Datos de equipos guardados
│
├── archivos.py             # Funciones para leer y guardar archivos JSON
├── estudiantes.py          # Lógica para registrar, validar y buscar estudiantes
├── equipos.py              # Lógica para registrar y buscar equipos
├── main.py                 # Menú principal interactivo de consola
├── GUIA_DE_ESTUDIO.md      # Guía de estudio paso a paso para aprender el código
└── README.md               # Este archivo de presentación
```

---

## 🛠️ Requisitos e Instalación

No necesitas instalar librerías externas. Todo funciona con la **librería estándar de Python**.

### Requisitos:
- **Python 3.8** o superior instalado en el equipo.

### ¿Cómo ejecutarlo?

1. Abre tu terminal en la carpeta del proyecto.
2. Ejecuta el archivo principal:

```bash
python main.py
```
*(O en Linux/Mac si usas python3:)*
```bash
python3 main.py
```

---

## 🎮 Ejemplo de Uso

Al iniciar el programa verás el menú interactivo:

```text
=================================================================
      SISTEMA DE GESTIÓN DE ESTUDIANTES Y EQUIPOS
=================================================================
 1. Registrar estudiante
 2. Listar estudiantes registrados
 3. Buscar estudiante (por documento o nombre)
 4. Salir
=================================================================
 Seleccione una opción (1-4): 
```

---
