import json
import os

CARPETA_DATOS = "datos"


def asegurar_carpeta_datos():

    if not os.path.exists(CARPETA_DATOS):
        os.makedirs(CARPETA_DATOS)


def leer_json(nombre_archivo):

    asegurar_carpeta_datos()
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)

    if not os.path.exists(ruta):
        guardar_json(nombre_archivo, [])
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            return []
    except:
        return []


def guardar_json(nombre_archivo, datos):

    asegurar_carpeta_datos()
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
        return True
    except:
        return False
