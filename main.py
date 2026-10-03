from core.app_loader import AppLoader

def main():

    loader = AppLoader()
    loader.load()

    if not loader.apps:
        print("No hay aplicaciones disponibles")
        return
    while True:
        print("\n=== MENÚ PRINCIPAL ===\n")

        print("0 - Para salir")
        for index, app in enumerate(loader.apps, start=1):
            print(f"{index} - {app.APP_NAME}")

        opcion = (input("Seleccione una opción:  "))

        if opcion == "0":
            break

        try:
            indice = int(opcion) - 1

        except ValueError:
            print("Opción no válida, no es un numero")
            continue
        if indice < 0 or indice >= len(loader.apps):
            print("Opción no válida, fuera de rango")
            continue


if __name__ == "__main__":
    main()
