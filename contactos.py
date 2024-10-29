class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
        print("GESTION DE CONTACTOS")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

contactos = []

while True:
    mostrar_menu()
    opcion = input("Elige una opcion")

    if opcion == "5":
        print("saliendo del programa")
        break
    
    if opcion == "1":
        nombre = input("ingresa el nombre")
        telefono = input("ingresa el telefono")
        contacto = Contacto(nombre,telefono)
        contactos.append(contacto)
        print("contacto agregado")

    elif opcion == "2":
        for c in contactos:
            print(f"nombre: {c.nombre}, Telefono: {c.telefono}")

    elif opcion == "3":
        nombre = input("ingrese el nombre a buscar")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"nombre: {c.nombre}, Telefono: {c.telefono}")
                encontrado = True
                break
            if not encontrado:
                print("contacto no encontrado")

    elif opcion == "4":
        nombre = input("ingrese el nombre a buscar")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("contacto eliminado")
                break
    
    else:
        print("opcion no valida")