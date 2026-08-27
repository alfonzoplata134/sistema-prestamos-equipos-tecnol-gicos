import archivos

NOMBRE_ARCHIVO = "equipos.json"


def cargar_equipos():
    """Carga la lista de equipos desde el archivo JSON."""
    return archivos.leer_json(NOMBRE_ARCHIVO)


def guardar_equipos(lista_equipos):
    """Guarda la lista de equipos en el archivo JSON."""
    return archivos.guardar_json(NOMBRE_ARCHIVO, lista_equipos)


def _limpiar_espacios(texto):
    """Elimina espacios al inicio, final y espacios dobles interiores."""
    return " ".join(str(texto).split())


def buscar_equipo_por_id(id_equipo):
    """Busca un equipo por su ID ignorando mayúsculas y espacios externos."""
    if not id_equipo:
        return None

    id_limpio = str(id_equipo).strip().upper()
    equipos = cargar_equipos()

    for equipo in equipos:
        if str(equipo.get("id_equipo", "")).strip().upper() == id_limpio:
            return equipo

    return None


def consultar_equipos():
    """Retorna todos los equipos registrados."""
    return cargar_equipos()


def registrar_equipo(id_equipo, tipo, marca, modelo, estado="disponible"):
    """Registra un nuevo equipo en el inventario con datos limpios y normalizados."""
    id_limpio = str(id_equipo).strip().upper()
    tipo_limpio = _limpiar_espacios(tipo).title()
    marca_limpio = _limpiar_espacios(marca).title()
    modelo_limpio = _limpiar_espacios(modelo).upper()
    estado_limpio = str(estado).strip().lower()

    # Validar campos vacíos
    if not id_limpio or not tipo_limpio or not marca_limpio or not modelo_limpio:
        return False, "Error: Todos los campos del equipo son obligatorios."

    # Validar que no existan espacios en el ID
    if " " in id_limpio:
        return False, "Error: El ID del equipo no debe contener espacios en blanco."

    # Validar que no exista un equipo con el mismo ID
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
    return False, "Error: No se pudo guardar el equipo en el archivo."
