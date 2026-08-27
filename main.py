import estudiantes


def limpiar_pantalla():
    """Imprime una línea divisoria para separar las pantallas."""
    print("\n" + "=" * 65)


def solicitar_campo_no_vacio(mensaje):
    """Pide un dato al usuario y no avanza hasta que escriba algo."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("   [!] Este campo es obligatorio. Por favor, ingrese un valor.")


def menu_registrar_estudiante():
    """Pide los datos de un estudiante y lo registra aplicando validaciones."""
    print("\n--- REGISTRAR NUEVO ESTUDIANTE ---")
    documento = solicitar_campo_no_vacio(" » Número de Documento (6 a 10 dígitos numéricos): ")
    nombre = solicitar_campo_no_vacio(" » Nombre Completo: ")
    correo = solicitar_campo_no_vacio(" » Correo Electrónico: ")
    programa = solicitar_campo_no_vacio(" » Programa Académico: ")

    print("\nProcesando registro...")
    exito, mensaje = estudiantes.registrar_estudiante(documento, nombre, correo, programa)

    if exito:
        print(f"\n [✓] ÉXITO: {mensaje}")
    else:
        print(f"\n [✗] ERROR: {mensaje}")


def menu_listar_estudiantes():
    """Muestra todos los estudiantes registrados en una tabla ordenada."""
    print("\n--- LISTADO DE ESTUDIANTES REGISTRADOS ---")
    lista = estudiantes.consultar_estudiantes()

    if not lista:
        print("\n [i] No hay estudiantes registrados en el sistema actualmente.")
        return

    print(f"\nTotal registrados: {len(lista)}")
    print("-" * 80)
    print(f"{'DOCUMENTO':<14} | {'NOMBRE':<25} | {'PROGRAMA':<18} | {'CORREO'}")
    print("-" * 80)

    for est in lista:
        doc = str(est.get("documento", ""))
        nom = str(est.get("nombre", ""))
        prog = str(est.get("programa", ""))
        mail = str(est.get("correo", ""))
        print(f"{doc:<14} | {nom:<25} | {prog:<18} | {mail}")

    print("-" * 80)


def menu_buscar_estudiante():
    """Permite buscar estudiantes por número de documento o por nombre."""
    print("\n--- BÚSQUEDA DE ESTUDIANTE ---")
    criterio = input(" » Ingrese el número de documento o nombre a buscar: ").strip()

    if not criterio:
        print(" [!] No ingresó ningún dato para la búsqueda.")
        return

    # 1. Intentar buscar primero por documento si ingresó números
    estudiante = estudiantes.buscar_estudiante_por_documento(criterio)

    if estudiante:
        print("\n [✓] Estudiante encontrado por documento:")
        print(" " + "-" * 45)
        print(f"   • Documento : {estudiante.get('documento')}")
        print(f"   • Nombre    : {estudiante.get('nombre')}")
        print(f"   • Correo    : {estudiante.get('correo')}")
        print(f"   • Programa  : {estudiante.get('programa')}")
        print(" " + "-" * 45)
        return

    # 2. Si no se encontró por documento, buscar por nombre (sin importar mayúsculas/espacios)
    coincidencias = estudiantes.buscar_estudiantes_por_nombre(criterio)

    if coincidencias:
        print(f"\n [✓] Se encontraron {len(coincidencias)} estudiante(s) con el nombre '{criterio}':")
        print(" " + "-" * 60)
        for idx, est in enumerate(coincidencias, start=1):
            print(f"   {idx}. {est.get('nombre')} | Doc: {est.get('documento')} | Prog: {est.get('programa')}")
            print(f"      Correo: {est.get('correo')}")
        print(" " + "-" * 60)
    else:
        print(f"\n [✗] No se encontró ningún estudiante con el criterio '{criterio}'.")


def mostrar_menu_principal():
    """Muestra las opciones del menú principal."""
    limpiar_pantalla()
    print("      SISTEMA DE PRÉSTAMOS DE EQUIPOS TECNOLÓGICOS")
    print("=" * 65)
    print(" 1. Registrar estudiante")
    print(" 2. Listar estudiantes registrados")
    print(" 3. Buscar estudiante (por documento o nombre)")
    print(" 4. Salir")
    print("=" * 65)


def main():
    """Bucle principal del programa."""
    while True:
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
            break
        else:
            print("\n [!] Opción no válida. Por favor, elija un número del 1 al 4.")

        input("\n Presione [ENTER] para continuar...")


if __name__ == "__main__":
    main()
