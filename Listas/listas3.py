import os,time
nombres_estudiantes=[]
os.system('cls')
while True:
    os.system('cls')
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
                time.sleep(2)
                continue
            elif tiene_numeros:
                print("Error, tu nombre no puede contener números.")
                time.sleep(2)
                continue
            else:
                nombres_estudiantes.append(nombre_estudiante)
                print("Estudiante agregado correctamente!")
                time.sleep(2)
                break
    elif opc=="2":
        if len(nombres_estudiantes) == 0:
            print("No hay nombres registrados. Vuelva a la opción 1 y reintente.")
            time.sleep(2)
            continue
        else:
            while True:
                busqueda_estudiante=input("Ingrese el nombre de el estudiante que desea encontrar:").strip().title()
                
                for letra in busqueda_estudiante:
                    if letra.isdigit():
                        tiene_numeros=True

                if len(busqueda_estudiante) < 3:
                    print("El nombre debe ser mayor que 3 carácteres")
                    time.sleep(2)
                    continue
                    
                elif tiene_numeros:
                    print("Error, el nombre no puede contener números.")
                    time.sleep(2)
                    continue
                   
                else:
                    if busqueda_estudiante in nombres_estudiantes:
                        print(f"El estudiante {busqueda_estudiante} se encuentra registrado en la lista.")
                        time.sleep(2)
                        break
    elif opc=="3":  
            if len(nombres_estudiantes) == 0:
                print("No hay nombres registrados. Vuelva a la opción 1 y reintente.")
                time.sleep(2)
                continue
            else:   
                while True:
                    eliminar_estudiante=input("Ingrese el nombre de el estudiante que desea eliminar:").strip().title()
                
                    for letra in eliminar_estudiante:
                        if letra.isdigit():
                            tiene_numeros=True

                    if len(eliminar_estudiante) < 3:
                        print("El nombre debe ser mayor que 3 carácteres")
                        time.sleep(2)
                        continue
                    elif tiene_numeros:
                        print("Error, el nombre no puede contener números.")
                        time.sleep(2)
                        continue
                    else:
                        if eliminar_estudiante in nombres_estudiantes:
                            nombres_estudiantes.remove(eliminar_estudiante)
                            print(f"El estudiante {eliminar_estudiante} se ha eliminado de la lista.")
                            time.sleep(2)
                            break
    elif opc=="4":
        if len(nombres_estudiantes)==0:
            print("No hay estudiantes registrados.")
            time.sleep(2)
            continue
        else:
            print("Estudiantes registrados: ")
            for estudiante in nombres_estudiantes:
                print(estudiante)
                time.sleep(2)
    elif opc=="5":
        print("Gracias por usar el menú, adiós")
        time.sleep(2)
        break
    else:
        print("Opción incorrecta reintentelo.")
        time.sleep(2)
        continue