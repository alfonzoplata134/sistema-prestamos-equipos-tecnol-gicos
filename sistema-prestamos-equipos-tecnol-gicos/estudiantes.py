import re
import archivos

NOMBRE_ARCHIVO = "estudiantes.json"


def cargar_estudiantes():

    return archivos.leer_json(NOMBRE_ARCHIVO)


def guardar_estudiantes(lista_estudiantes):

    return archivos.guardar_json(NOMBRE_ARCHIVO, lista_estudiantes)


def _limpiar_espacios(texto):

    return " ".join(str(texto).split())


def _validar_formato_correo(correo):

    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo))


def validar_documento(documento):

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

    if not documento:
        return None

    doc_limpio = str(documento).strip()
    estudiantes = cargar_estudiantes()

    for estudiante in estudiantes:
        if str(estudiante.get("documento", "")).strip() == doc_limpio:
            return estudiante

    return None


def buscar_estudiantes_por_nombre(nombre):

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

    doc_valido, resultado_doc = validar_documento(documento)
    if not doc_valido:
        return False, resultado_doc
    doc_limpio = resultado_doc

    nombre_limpio = _limpiar_espacios(nombre).title()
    if not nombre_limpio:
        return False, "Error: El nombre del estudiante es obligatorio."
    if not all(c.isalpha() or c.isspace() for c in nombre_limpio):
        return False, "Error: El nombre debe contener únicamente letras y espacios."

    correo_limpio = str(correo).strip().lower()
    if not correo_limpio:
        return False, "Error: El correo electrónico es obligatorio."
    if not _validar_formato_correo(correo_limpio):
        return False, f"Error: El formato del correo '{correo_limpio}' es inválido (ejemplo: usuario@correo.com)."

    programa_limpio = _limpiar_espacios(programa).title()
    if not programa_limpio:
        return False, "Error: El programa académico es obligatorio."
    if not all(c.isalpha() or c.isspace() or c in ".-()" for c in programa_limpio):
        return False, "Error: El programa académico debe contener únicamente letras, espacios, puntos o guiones."

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
