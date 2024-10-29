class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

tareas = []

def mostrar_menu():
    print("GESTIÓN DE TAREAS")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de tarea a completada")
    print("5. Eliminar tarea por título")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "6":
        print("Saliendo del programa.")
        break

    elif opcion == "1":
        try:
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            tarea = Tarea(titulo, descripcion)
            tareas.append(tarea)
            print("Tarea agregada exitosamente.")
        except ValueError:
            print("Error: Por favor, ingrese valores válidos.")

    elif opcion == "2":
        if tareas:
            print("Lista de tareas:")
            for t in tareas:
                print(t)
        else:
            print("No hay tareas en la lista.")

    elif opcion == "3":
        titulo = input("Ingrese el título de la tarea a buscar: ")
        encontrado = False
        for t in tareas:
            if t.titulo.lower() == titulo.lower():
                print("Tarea encontrada:")
                print(t)
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")

    elif opcion == "4":
        titulo = input("Ingrese el título de la tarea para marcar como completada: ")
        encontrado = False
        for t in tareas:
            if t.titulo.lower() == titulo.lower():
                t.completada = True
                print("Estado de la tarea actualizado a 'completada'.")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")

    elif opcion == "5":
        titulo = input("Ingrese el título de la tarea a eliminar: ")
        encontrado = False
        for t in tareas:
            if t.titulo.lower() == titulo.lower():
                tareas.remove(t)
                print("Tarea eliminada exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")

    else:
        print("Opción no válida. Intente de nuevo.")
