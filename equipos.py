from typing import Dict, List, Optional, Tuple
import archivos

NOMBRE_ARCHIVO = "equipos.json"


def cargar_equipos() -> List[Dict[str, str]]:
    return archivos.leer_json(NOMBRE_ARCHIVO)


def guardar_equipos(lista_equipos: List[Dict[str, str]]) -> bool:
    return archivos.guardar_json(NOMBRE_ARCHIVO, lista_equipos)


def buscar_equipo_por_id(id_equipo: str) -> Optional[Dict[str, str]]:
    if not id_equipo or not isinstance(id_equipo, str):
        return None

    id_limpio = id_equipo.strip().upper()
    equipos = cargar_equipos()
    for equipo in equipos:
        if equipo.get("id_equipo", "").strip().upper() == id_limpio:
            return equipo
    return None


def consultar_equipos() -> List[Dict[str, str]]:
    return cargar_equipos()


def registrar_equipo(
    id_equipo: str,
    tipo: str,
    marca: str,
    modelo: str,
    estado: str = "disponible"
) -> Tuple[bool, str]:
    id_limpio = id_equipo.strip().upper()
    tipo_limpio = tipo.strip()
    marca_limpio = marca.strip()
    modelo_limpio = modelo.strip()
    estado_limpio = estado.strip().lower()

    if not id_limpio or not tipo_limpio or not marca_limpio or not modelo_limpio:
        return False, "Error de validación: Todos los campos del equipo son obligatorios."

    if buscar_equipo_por_id(id_limpio) is not None:
        return False, f"Error: Ya existe un equipo registrado con el ID '{id_limpio}'."

    equipos = cargar_equipos()
    nuevo_equipo = {
        "id_equipo": id_limpio,
        "tipo": tipo_limpio,
        "marca": marca_limpio,
        "modelo": modelo_limpio,
        "estado": estado_limpio
    }

    equipos.append(nuevo_equipo)
    if guardar_equipos(equipos):
        return True, f"Equipo '{id_limpio}' ({tipo_limpio} {marca_limpio}) registrado exitosamente."
    return False, "Error crítico: No se pudo guardar el equipo en el archivo JSON."
