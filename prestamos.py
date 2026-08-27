from typing import Dict, List, Optional, Tuple
import archivos
import estudiantes
import equipos

NOMBRE_ARCHIVO = "prestamos.json"


def cargar_prestamos() -> List[Dict[str, str]]:
    return archivos.leer_json(NOMBRE_ARCHIVO)


def guardar_prestamos(lista_prestamos: List[Dict[str, str]]) -> bool:
    return archivos.guardar_json(NOMBRE_ARCHIVO, lista_prestamos)


def buscar_prestamo_por_id(id_prestamo: str) -> Optional[Dict[str, str]]:
    if not id_prestamo or not isinstance(id_prestamo, str):
        return None

    id_limpio = id_prestamo.strip().upper()
    prestamos = cargar_prestamos()
    for prestamo in prestamos:
        if prestamo.get("id_prestamo", "").strip().upper() == id_limpio:
            return prestamo
    return None


def consultar_prestamos() -> List[Dict[str, str]]:
    return cargar_prestamos()


def registrar_prestamo(
    id_prestamo: str,
    documento_estudiante: str,
    id_equipo: str,
    fecha_prestamo: str,
    estado: str = "activo"
) -> Tuple[bool, str]:
    id_pres_limpio = id_prestamo.strip().upper()
    doc_limpio = documento_estudiante.strip()
    id_eq_limpio = id_equipo.strip().upper()
    fecha_limpia = fecha_prestamo.strip()

    if not all([id_pres_limpio, doc_limpio, id_eq_limpio, fecha_limpia]):
        return False, "Error de validación: Todos los campos del préstamo son obligatorios."

    if estudiantes.buscar_estudiante_por_documento(doc_limpio) is None:
        return False, f"Error: No existe ningún estudiante registrado con el documento '{doc_limpio}'."

    equipo = equipos.buscar_equipo_por_id(id_eq_limpio)
    if equipo is None:
        return False, f"Error: No existe ningún equipo con el ID '{id_eq_limpio}'."

    if buscar_prestamo_por_id(id_pres_limpio) is not None:
        return False, f"Error: Ya existe un préstamo con el ID '{id_pres_limpio}'."

    prestamos = cargar_prestamos()
    nuevo_prestamo = {
        "id_prestamo": id_pres_limpio,
        "documento_estudiante": doc_limpio,
        "id_equipo": id_eq_limpio,
        "fecha_prestamo": fecha_limpia,
        "estado": estado.strip().lower()
    }

    prestamos.append(nuevo_prestamo)
    if guardar_prestamos(prestamos):
        return True, f"Préstamo '{id_pres_limpio}' registrado con éxito."
    return False, "Error crítico: No se pudo guardar el registro del préstamo."
