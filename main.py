import sys
import estudiantes


def limpiar_pantalla() -> None:
    """============================================."""
    print("\n" + "=" * 65)


def solicitar_campo_no_vacio(etiqueta: str) -> str:
    """Solicita al usuario un dato y valida que no esté vacío."""
    while True:
        try:
            valor = input(etiqueta).strip()
            if valor:
                return valor
            print("   [!] Este campo es obligatorio. Por favor, ingrese un valor.")
        except (KeyboardInterrupt, EOFError):
            print("\n   [!] Operación cancelada por el usuario.")
            raise


def menu_registrar_estudiante() -> None:
    """Gestiona el registro de un nuevo estudiante."""
    print("\n--- REGISTRAR NUEVO ESTUDIANTE ---")
    try:
        documento = solicitar_campo_no_vacio(" » Número de Documento (sin espacios): ")
        nombre = solicitar_campo_no_vacio(" » Nombre Completo: ")
        correo = solicitar_campo_no_vacio(" » Correo Electrónico: ")
        programa = solicitar_campo_no_vacio(" » Programa Académico: ")

        print("\n Procesando registro...")
        exito, mensaje = estudiantes.registrar_estudiante(
            documento=documento,
            nombre=nombre,
            correo=correo,
            programa=programa
        )

        if exito:
            print(f"\n [✓] ÉXITO: {mensaje}")
        else:
            print(f"\n [✗] ERROR: {mensaje}")

    except (KeyboardInterrupt, EOFError):
        print("\n [!] Registro de estudiante abortado.")


def menu_listar_estudiantes() -> None:
    """Muestra la lista de estudiantes registrados."""
    print("\n--- LISTADO DE ESTUDIANTES REGISTRADOS ---")
    lista = estudiantes.consultar_estudiantes()

    if not lista:
        print("\n [i] No hay estudiantes registrados en el sistema actualmente.")
        return

    print(f"\nTotal registrados: {len(lista)}")
    print("-" * 80)
    print(f"{'DOCUMENTO':<15} | {'NOMBRE':<25} | {'PROGRAMA':<20} | {'CORREO'}")
    print("-" * 80)

    for est in lista:
        doc = est.get("documento", "N/A")[:14]
        nom = est.get("nombre", "N/A")[:24]
        prog = est.get("programa", "N/A")[:19]
        mail = est.get("correo", "N/A")
        print(f"{doc:<15} | {nom:<25} | {prog:<20} | {mail}")
    
    print("-" * 80)


def menu_buscar_estudiante() -> None:
    """Permite buscar un estudiante por su número de documento."""
    print("\n--- BÚSQUEDA DE ESTUDIANTE POR DOCUMENTO ---")
    try:
        documento = input(" » Ingrese el número de documento a consultar: ").strip()
        if not documento:
            print(" [!] No ingresó ningún documento para la búsqueda.")
            return

        estudiante = estudiantes.buscar_estudiante_por_documento(documento)

        if estudiante:
            print("\n [✓] Estudiante encontrado:")
            print(" " + "-" * 45)
            print(f"   • Documento : {estudiante.get('documento')}")
            print(f"   • Nombre    : {estudiante.get('nombre')}")
            print(f"   • Correo    : {estudiante.get('correo')}")
            print(f"   • Programa  : {estudiante.get('programa')}")
            print(" " + "-" * 45)
        else:
            print(f"\n [✗] No se encontró ningún estudiante con el documento '{documento}'.")

    except (KeyboardInterrupt, EOFError):
        print("\n [!] Búsqueda cancelada.")


def mostrar_menu_principal() -> None:

    limpiar_pantalla()
    print("      SISTEMA DE PRÉSTAMOS DE EQUIPOS TECNOLÓGICOS")
    print("=" * 65)
    print(" 1. Registrar estudiante")
    print(" 2. Listar estudiantes registrados")
    print(" 3. Buscar estudiante por documento")
    print(" 4. Salir")
    print("=" * 65)


def main() -> None:
    """Ejecuta el flujo principal del sistema de préstamos."""
    while True:
        try:
            mostrar_menu_principal()
            opcion = input(" Seleccione una opción (1-4): ").strip()

            if opcion == "1":
                menu_registrar_estudiante()
            elif opcion == "2":
                menu_listar_estudiantes()
            elif opcion == "3":
                menu_buscar_estudiante()
            elif opcion == "4":
                print("\n Gracias por utilizar el Sistema de Préstamos. ¡Hasta pronto!\n")
                sys.exit(0)
            else:
                print("\n [!] Opción no válida. Por favor, ingrese un número del 1 al 4.")

            input("\n Presione [ENTER] para continuar...")

        except (KeyboardInterrupt, EOFError):
            print("\n\n Sesión finalizada por el usuario. ¡Hasta pronto!\n")
            sys.exit(0)
        except Exception as e:
            print(f"\n [!] Ocurrió un error imprevisto: {e}")
            input("\n Presione [ENTER] para continuar...")


if __name__ == "__main__":
    main()
