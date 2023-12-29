# Importa la biblioteca para formatear números en moneda
import locale

# Establece la configuración de localización chile
locale.setlocale(locale.LC_ALL, "es_CL")

# función agregar_compra
def agregar_compra(compra, compras):
    # Agrega la compra a la lista
    compras.append(compra)

    # Muestra un mensaje de confirmación
    print("Compra agregada correctamente")

# función mostrar_compras
def mostrar_compras(compras):
    # Si la lista de compras está vacía, muestra un mensaje
    if not compras:
        print("No hay compras registradas")
        return

    # Recorre la lista de compras y muestra cada compra
    for i, compra in enumerate(compras):
        # Muestra el número y el monto de la compra, le sumamos +1 ya que parte en 0
        print(f"Compra {i + 1}: {compra}")

# función mostrar_total
def mostrar_total(compras):
    # Si la lista de compras está vacía, muestra un mensaje
    if not compras:
        print("No hay compras registradas")
        return

    # Calcula el total gastado
    total_gastado = 0
    for compra in compras:
        total_gastado += compra

    # Formatea el total gastado
    total_gastado = locale.currency(total_gastado, grouping=True)

    # Muestra el total gastado
    print(f"Total gastado: {total_gastado}")

# Define la función main()
def main():
    # Crea una lista vacía de compras
    compras = []

    # Crea una variable que almacena el total gastado
    total_gastado = 0

    # Crea un bucle while True
    while True:
        # Muestra el menú
        print("** Menú **")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        # Solicitar al usuario el ingreso de una opcion
        opcion = input("Seleccione una opción: ")

        # Verifica la opción seleccionada por el usuario
        if opcion == "1":
            # Solicita al usuario el monto de la compra
            monto = int(input("Ingrese el monto de la compra: "))

            # Agrega la compra a la lista
            agregar_compra(monto, compras)

        elif opcion == "2":
            # Muestra las compras
            mostrar_compras(compras)

        elif opcion == "3":
            # Muestra el total gastado
            mostrar_total(compras)

        elif opcion == "4":
            # Termina el programa
            break

        else:
            # Muestra un mensaje de error
            print("Opción incorrecta")

# Llama a la función main()
if __name__ == "__main__":
    main()