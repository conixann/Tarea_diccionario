nombres_estudiantes=[]
while True:
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Mostrar estudiante")
    print("5. Salir")
    opc=input("Seleccione una opción: ")
    if opc=="1":
        while True:
            print("Agregar estudiante.")
            nombre_estudiante=input("Ingrese el nombre de el estudiante: ").strip().title()
            tiene_numeros=False
            
            for letra in nombre_estudiante:
                if letra.isdigit():
                    tiene_numeros=True    

            if len(nombre_estudiante) < 3:
                print("El nombre debe ser mayor que 3 carácteres")
                continue
            elif tiene_numeros:
                print("Error, tu nombre no puede contener números.")
                continue
            else:
                nombres_estudiantes.append(nombre_estudiante)
                print("Estudiante agregado correctamente!")
                break
    elif opc=="2":
        if len(nombres_estudiantes) == 0:
            print("No hay nombres registrados. Vuelva a la opción 1 y reintente.")
            continue
        else:
            while True:
                busqueda_estudiante=input("Ingrese el nombre de el estudiante que desea encontrar:").strip().title()
                
                for letra in busqueda_estudiante:
                    if letra.isdigit():
                        tiene_numeros=True

                if busqueda_estudiante < 3:
                    print("El nombre debe ser mayor que 3 carácteres")
                    continue
                elif tiene_numeros:
                    print("Error, el nombre no puede contener números.")
                    continue
                else:
                    if busqueda_estudiante in nombres_estudiantes:
                        print(f"El estudiante {busqueda_estudiante} se encuentra registrado en la lista.")
                        break

    elif opc=="3":
        pass
    elif opc=="4":
        pass
    elif opc=="5":
        print("Gracias por usar el menú, adiós")
    else:
        print("Opción incorrecta reintentelo.")
        continue