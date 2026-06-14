import os,time
def mostrar_menu():
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Mostrar estudiante")
    print("5. Salir")

def leer_opcion():
    while True:
        try:
            opc=int(input("Ingrese una opción (1-5): "))
            if opc >=1 and opc <=5:
                return opc
            print("Error, debe ingresar una opción válida.")
        except ValueError:
            print("Error! debe ingresar un número entero!")

def validar_nombre():
        while True:

            nombre = input("Ingrese el nombre: ").strip().title()

            tiene_numeros = False

            for letra in nombre:
                if letra.isdigit():
                    tiene_numeros = True

            if len(nombre) < 3:
                print("Error")
                continue
            elif tiene_numeros:
                print("Error")
                continue
            else:
                return nombre
                
            
def agregar_estudiante():

    nombre = validar_nombre()

    nombres_estudiantes.append(nombre)

    print("Estudiante agregado correctamente")

def buscar_estudiante():
    if len(nombres_estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    nombre = validar_nombre()

    if nombre in nombres_estudiantes:
        print("Encontrado")
    else:
        print("No encontrado")

def eliminar_estudiante():
    if len(nombres_estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    nombre = validar_nombre()

    if nombre in nombres_estudiantes:
        nombres_estudiantes.remove(nombre)

def mostrar_estudiantes():
    if len(nombres_estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("Estudiantes registrados:")
        for estudiante in nombres_estudiantes:
            print(estudiante)

nombres_estudiantes=[]

while True:
    os.system('cls')
    mostrar_menu()
    opc=leer_opcion()
    if opc==1:
        agregar_estudiante()
    elif opc==2:
        buscar_estudiante()
    elif opc==3:
        eliminar_estudiante()
    elif opc==4:
        mostrar_estudiantes()
    elif opc==5:
        print("Gracias por usar el programa, adiós")
        break
    else:
        print("Opción inválida, intente nuevamente")