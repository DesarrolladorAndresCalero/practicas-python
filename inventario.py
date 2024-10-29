class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

productos = []

def mostrar_menu():
    print("SISTEMA DE INVENTARIO")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por nombre")
    print("4. Actualizar cantidad de producto")
    print("5. Eliminar producto")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "6":
        print("Saliendo del programa.")
        break

    elif opcion == "1":
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(nombre, cantidad, precio)
            productos.append(producto)
            print("Producto agregado exitosamente.")
        except ValueError:
            print("Error: Por favor, ingrese valores válidos para la cantidad y el precio.")

    elif opcion == "2":
        if productos:
            print("Lista de productos:")
            for p in productos:
                print(p)
        else:
            print("No hay productos en la lista.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for p in productos:
            if p.nombre.lower() == nombre.lower():
                print("Producto encontrado:")
                print(p)
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto para actualizar cantidad: ")
        encontrado = False
        for p in productos:
            if p.nombre.lower() == nombre.lower():
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    p.cantidad = nueva_cantidad
                    print("Cantidad actualizada exitosamente.")
                    encontrado = True
                except ValueError:
                    print("Error: Por favor, ingrese un valor válido para la cantidad.")
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        for p in productos:
            if p.nombre.lower() == nombre.lower():
                productos.remove(p)
                print("Producto eliminado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    else:
        print("Opción no válida. Intente de nuevo.")
