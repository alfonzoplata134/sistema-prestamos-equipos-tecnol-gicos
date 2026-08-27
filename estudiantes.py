import archivos

NOMBRE_ARCHIVO = "estudiantes.json"


def cargar_estudiantes():
    """Carga la lista de estudiantes desde el archivo JSON."""
    return archivos.leer_json(NOMBRE_ARCHIVO)


def guardar_estudiantes(lista_estudiantes):
    """Guarda la lista de estudiantes en el archivo JSON."""
    return archivos.guardar_json(NOMBRE_ARCHIVO, lista_estudiantes)


def _limpiar_espacios(texto):
    """Elimina espacios al inicio, final y espacios dobles interiores."""
    return " ".join(str(texto).split())


def _validar_formato_correo(correo):
    """Valida de forma simple que el correo tenga @, punto y no tenga espacios."""
    if "@" in correo and "." in correo and " " not in correo:
        partes = correo.split("@")
        if len(partes) == 2 and partes[0] and partes[1]:
            return "." in partes[1]
    return False


def validar_documento(documento):
    """
    Valida que el documento:
    1. No esté vacío
    2. No tenga espacios en blanco
    3. Contenga solo números (sin letras)
    4. Tenga entre 6 y 10 dígitos
    Retorna: (es_valido: bool, resultado_o_error: str)
    """
    if documento is None:
        return False, "Error: El número de documento es obligatorio."

    doc_str = str(documento).strip()

    if not doc_str:
        return False, "Error: El número de documento no puede estar vacío."

    if " " in doc_str:
        return False, "Error: El documento no debe contener espacios en blanco."

    if not doc_str.isdigit():
        return False, "Error: El documento debe contener únicamente números (sin letras ni símbolos)."

    if len(doc_str) < 6 or len(doc_str) > 10:
        return False, f"Error: El documento debe tener entre 6 y 10 dígitos (ingresó {len(doc_str)} dígitos)."

    return True, doc_str


def buscar_estudiante_por_documento(documento):
    """Busca un estudiante por su documento exacto (ignorando espacios alrededor)."""
    if not documento:
        return None

    doc_limpio = str(documento).strip()
    estudiantes = cargar_estudiantes()

    for estudiante in estudiantes:
        if str(estudiante.get("documento", "")).strip() == doc_limpio:
            return estudiante

    return None


def buscar_estudiantes_por_nombre(nombre):
    """
    Busca estudiantes por nombre sin importar mayúsculas, minúsculas ni espacios extra.
    Retorna una lista con todas las coincidencias.
    """
    if not nombre:
        return []

    nombre_busqueda = _limpiar_espacios(nombre).lower()
    estudiantes = cargar_estudiantes()
    coincidencias = []

    for est in estudiantes:
        nom_estudiante = _limpiar_espacios(est.get("nombre", "")).lower()
        if nombre_busqueda in nom_estudiante:
            coincidencias.append(est)

    return coincidencias


def consultar_estudiantes():
    """Retorna todos los estudiantes registrados."""
    return cargar_estudiantes()


def registrar_estudiante(documento, nombre, correo, programa):
    """Registra un nuevo estudiante aplicando todas las validaciones solicitadas."""
    # 1. Validar documento (sin espacios, sin letras, entre 6 y 10 dígitos)
    doc_valido, resultado_doc = validar_documento(documento)
    if not doc_valido:
        return False, resultado_doc
    doc_limpio = resultado_doc

    # 2. Validar y normalizar nombre (eliminar espacios extra y poner en formato Título)
    nombre_limpio = _limpiar_espacios(nombre).title()
    if not nombre_limpio:
        return False, "Error: El nombre del estudiante es obligatorio."

    # 3. Validar y normalizar correo electrónico
    correo_limpio = str(correo).strip().lower()
    if not correo_limpio:
        return False, "Error: El correo electrónico es obligatorio."
    if not _validar_formato_correo(correo_limpio):
        return False, f"Error: El formato del correo '{correo_limpio}' es inválido (ejemplo: usuario@correo.com)."

    # 4. Validar y normalizar programa académico
    programa_limpio = _limpiar_espacios(programa).title()
    if not programa_limpio:
        return False, "Error: El programa académico es obligatorio."

    # 5. Validar que no exista un estudiante con el mismo documento
    if buscar_estudiante_por_documento(doc_limpio) is not None:
        return False, f"Error: Ya existe un estudiante registrado con el documento '{doc_limpio}'."

    estudiantes = cargar_estudiantes()
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
        return False, "Error: No se pudo guardar la información en el archivo."
