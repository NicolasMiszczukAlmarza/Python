from pathlib import Path
import os
import shutil


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

RUTA_RECETAS = Path(__file__).parent


# ==========================================================
# FUNCIONES GENERALES
# ==========================================================

def limpiar_pantalla():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """Espera antes de regresar al menú."""
    input("\nPresiona Enter para volver al menú...")


def contar_recetas():
    """Cuenta todos los archivos .txt de las categorías."""
    return len(list(RUTA_RECETAS.glob("**/*.txt")))


# ==========================================================
# CATEGORÍAS
# ==========================================================

def obtener_categorias():
    """Obtiene todas las carpetas de categorías."""
    categorias = []

    for elemento in RUTA_RECETAS.iterdir():
        if elemento.is_dir():
            categorias.append(elemento)

    return sorted(categorias, key=lambda categoria: categoria.name.lower())


def mostrar_categorias(categorias):
    """Muestra las categorías disponibles."""

    print("\n--- CATEGORÍAS ---")

    for numero, categoria in enumerate(categorias, start=1):
        print(f"{numero}. {categoria.name}")


def elegir_categoria():
    """Permite al usuario elegir una categoría."""

    categorias = obtener_categorias()

    if not categorias:
        print("\nNo hay categorías disponibles.")
        return None

    mostrar_categorias(categorias)

    while True:

        try:
            opcion = int(input("\nElige una categoría: "))

            if 1 <= opcion <= len(categorias):
                return categorias[opcion - 1]

            print("Categoría no válida.")

        except ValueError:
            print("Debes introducir un número.")


def crear_categoria():
    """Crea una nueva categoría."""

    nombre = input("\nNombre de la nueva categoría: ").strip()

    if not nombre:
        print("\nEl nombre no puede estar vacío.")
        return

    nueva_categoria = RUTA_RECETAS / nombre

    if nueva_categoria.exists():
        print("\nEsa categoría ya existe.")
        return

    nueva_categoria.mkdir()

    print(f"\nCategoría '{nombre}' creada correctamente.")


def eliminar_categoria():
    """Elimina una categoría."""

    categoria = elegir_categoria()

    if categoria is None:
        return

    confirmar = input(
        f"\n¿Quieres eliminar '{categoria.name}' "
        f"y todas sus recetas? (s/n): "
    ).strip().lower()

    if confirmar == "s":

        shutil.rmtree(categoria)

        print("\nCategoría eliminada correctamente.")

    else:
        print("\nOperación cancelada.")


# ==========================================================
# RECETAS
# ==========================================================

def obtener_recetas(categoria):
    """Obtiene las recetas de una categoría."""

    recetas = []

    for archivo in categoria.iterdir():

        if archivo.is_file() and archivo.suffix == ".txt":
            recetas.append(archivo)

    return sorted(recetas, key=lambda receta: receta.name.lower())


def mostrar_recetas(recetas):
    """Muestra las recetas disponibles."""

    print("\n--- RECETAS ---")

    for numero, receta in enumerate(recetas, start=1):
        print(f"{numero}. {receta.stem}")


def elegir_receta(categoria):
    """Permite elegir una receta."""

    recetas = obtener_recetas(categoria)

    if not recetas:
        print("\nNo hay recetas en esta categoría.")
        return None

    mostrar_recetas(recetas)

    while True:

        try:
            opcion = int(input("\nElige una receta: "))

            if 1 <= opcion <= len(recetas):
                return recetas[opcion - 1]

            print("Receta no válida.")

        except ValueError:
            print("Debes introducir un número.")


def leer_receta():
    """Lee una receta."""

    categoria = elegir_categoria()

    if categoria is None:
        return

    receta = elegir_receta(categoria)

    if receta is None:
        return

    contenido = receta.read_text(encoding="utf-8")

    print("\n" + "=" * 40)
    print(receta.stem.upper())
    print("=" * 40)

    print(contenido)


def crear_receta():
    """Crea una nueva receta."""

    categoria = elegir_categoria()

    if categoria is None:
        return

    nombre = input("\nNombre de la receta: ").strip()

    if not nombre:
        print("\nEl nombre no puede estar vacío.")
        return

    if nombre.lower().endswith(".txt"):
        nombre = nombre[:-4]

    nueva_receta = categoria / f"{nombre}.txt"

    if nueva_receta.exists():
        print("\nEsa receta ya existe.")
        return

    contenido = input("\nEscribe el contenido de la receta:\n")

    nueva_receta.write_text(
        contenido,
        encoding="utf-8"
    )

    print(f"\nReceta '{nombre}' creada correctamente.")


def eliminar_receta():
    """Elimina una receta."""

    categoria = elegir_categoria()

    if categoria is None:
        return

    receta = elegir_receta(categoria)

    if receta is None:
        return

    confirmar = input(
        f"\n¿Quieres eliminar '{receta.stem}'? (s/n): "
    ).strip().lower()

    if confirmar == "s":

        receta.unlink()

        print("\nReceta eliminada correctamente.")

    else:
        print("\nOperación cancelada.")


# ==========================================================
# MENÚ
# ==========================================================

def mostrar_menu():
    """Muestra el menú principal."""

    print("=" * 45)
    print("       ADMINISTRADOR DE RECETAS")
    print("=" * 45)

    print(f"\nRuta: {RUTA_RECETAS}")
    print(f"Total de recetas: {contar_recetas()}")

    print("""
---------------- MENÚ ----------------

1. Leer receta
2. Crear receta
3. Crear categoría
4. Eliminar receta
5. Eliminar categoría
6. Salir

--------------------------------------
""")


def pedir_opcion():
    """Solicita una opción válida del menú."""

    while True:

        try:
            opcion = int(input("Selecciona una opción: "))

            if 1 <= opcion <= 6:
                return opcion

            print("Elige una opción entre 1 y 6.")

        except ValueError:
            print("Debes introducir un número.")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    while True:

        limpiar_pantalla()

        mostrar_menu()

        opcion = pedir_opcion()

        # Equivalente al switch de otros lenguajes
        match opcion:

            case 1:
                leer_receta()

            case 2:
                crear_receta()

            case 3:
                crear_categoria()

            case 4:
                eliminar_receta()

            case 5:
                eliminar_categoria()

            case 6:
                print("\nGracias por usar el administrador de recetas.")
                print("¡Hasta pronto!")
                break

        pausar()


# ==========================================================
# INICIO
# ==========================================================

if __name__ == "__main__":
    main()