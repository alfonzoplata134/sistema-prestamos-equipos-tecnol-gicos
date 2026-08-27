import json
import os

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
DIRECTORIO_DATOS = os.path.join(DIRECTORIO_BASE, "datos")


def asegurar_directorio_datos() -> None:
    if not os.path.exists(DIRECTORIO_DATOS):
        os.makedirs(DIRECTORIO_DATOS, exist_ok=True)


def _obtener_ruta_completa(nombre_archivo: str) -> str:
    asegurar_directorio_datos()
    return os.path.join(DIRECTORIO_DATOS, nombre_archivo)


def leer_json(nombre_archivo: str) -> list:
    ruta = _obtener_ruta_completa(nombre_archivo)
    
    if not os.path.isfile(ruta):
        guardar_json(nombre_archivo, [])
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
            if isinstance(contenido, list):
                return contenido
            guardar_json(nombre_archivo, [])
            return []
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        guardar_json(nombre_archivo, [])
        return []


def guardar_json(nombre_archivo: str, datos: list) -> bool:
    ruta = _obtener_ruta_completa(nombre_archivo)
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except (TypeError, OSError):
        return False
