"""
Módulo para la gestión de estudiantes.

Permite registrar y manejar la información de los estudiantes
correspondiente a la HU03 del proyecto.
"""

import re
from typing import Dict, List, Optional, Tuple
import archivos

NOMBRE_ARCHIVO = "estudiantes.json"
REGEX_CORREO = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"


def cargar_estudiantes() -> List[Dict[str, str]]:
    return archivos.leer_json(NOMBRE_ARCHIVO)


def guardar_estudiantes(lista_estudiantes: List[Dict[str, str]]) -> bool:
    return archivos.guardar_json(NOMBRE_ARCHIVO, lista_estudiantes)


def _validar_formato_correo(correo: str) -> bool:
    if not isinstance(correo, str):
        return False
    return bool(re.match(REGEX_CORREO, correo.strip()))


def buscar_estudiante_por_documento(documento: str) -> Optional[Dict[str, str]]:
    if not documento or not isinstance(documento, str):
        return None
        
    doc_limpio = documento.strip()
    estudiantes = cargar_estudiantes()
    
    for estudiante in estudiantes:
        if estudiante.get("documento", "").strip() == doc_limpio:
            return estudiante
            
    return None


def consultar_estudiantes() -> List[Dict[str, str]]:
    return cargar_estudiantes()


def registrar_estudiante(
    documento: str,
    nombre: str,
    correo: str,
    programa: str
) -> Tuple[bool, str]:
    if not all(isinstance(v, str) for v in (documento, nombre, correo, programa)):
        return False, "Error de validación: Todos los campos deben ser cadenas de texto."

    doc_limpio = documento.strip()
    nombre_limpio = nombre.strip()
    correo_limpio = correo.strip()
    programa_limpio = programa.strip()

    if not doc_limpio:
        return False, "Error de validación: El número de documento es obligatorio y no puede estar vacío."
    
    if not nombre_limpio:
        return False, "Error de validación: El nombre del estudiante es obligatorio y no puede estar vacío."

    if not correo_limpio:
        return False, "Error de validación: El correo electrónico es obligatorio y no puede estar vacío."

    if not programa_limpio:
        return False, "Error de validación: El programa académico es obligatorio y no puede estar vacío."

    if " " in doc_limpio:
        return False, "Error de validación: El documento no debe contener espacios en blanco."

    if not _validar_formato_correo(correo_limpio):
        return False, f"Error de validación: El formato del correo '{correo_limpio}' es inválido (ejemplo válido: usuario@dominio.com)."

    estudiantes = cargar_estudiantes()
    for est in estudiantes:
        if est.get("documento", "").strip() == doc_limpio:
            return False, f"Error: Ya existe un estudiante registrado con el documento '{doc_limpio}'."

    nuevo_estudiante = {
        "documento": doc_limpio,
        "nombre": nombre_limpio,
        "correo": correo_limpio,
        "programa": programa_limpio
    }

    estudiantes.append(nuevo_estudiante)

    if guardar_estudiantes(estudiantes):
        return True, f"Estudiante '{nombre_limpio}' (Doc: {doc_limpio}) registrado exitosamente."
    else:
        return False, "Error crítico: No se pudo guardar la información en el archivo de almacenamiento."
