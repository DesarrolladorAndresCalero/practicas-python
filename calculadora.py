def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return "error de division"

def mostrar_menu():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

while True:
    mostrar_menu()
    opcion = input("Elige una opcion")

    if opcion == "5":
        print("saliendo del programa")
        break

    if opcion in ["1","2","3","4"]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
                print(f"Resultado: {suma(num1,num2)}")

        elif opcion == '2':
                print(f"Resultado: {resta(num1,num2)}")

        elif opcion == '3':
                print(f"Resultado: {multiplicacion(num1,num2)}")

        elif opcion == '4':
                print(f"Resultado: {division(num1,num2)}")
        else:
            print("Opción no válida. Intente de nuevo.")