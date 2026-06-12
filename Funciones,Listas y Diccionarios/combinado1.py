import os,time
estudiantes={}
os.system('cls')
while True:
    os.system('cls')
    print("Menú")
    print("1. Agregar estudiante")
    print("2. Agregar nota")
    print("3. Mostrar estudiantes")
    print("4. Mostrar promedio de un estudiante")
    print("5. Mostrar todos los promedios")
    print("6. Salir")
    opc=input("Ingrese opción: ")
    if opc=="1":
        while True:
                print("**Agregar nombre de estudiante**")
                nombre_estudiante=input("Ingrese nombre de el estudiante: ").strip().title()
                
            
                tiene_numero=False
                for letra in nombre_estudiante:
                    if letra.isdigit():
                        tiene_numero=True

                if  len(nombre_estudiante) < 3:
                    print("Error, el nombre debe ser más largo (3 caracteres como mínimo)")
                    time.sleep(2)
                    continue
                elif nombre_estudiante in estudiantes:
                    print("Error, el nombre de el estudiante ya existe")
                    time.sleep(2)
                    continue
                elif tiene_numero:
                    print("Error, el nombre no puede contener números")
                    time.sleep(2)
                    continue
                else:
                    estudiantes[nombre_estudiante] = []
                    print("El estudiante fue agregado exitosamente")
                    time.sleep(2)
                break
    elif opc=="2":
            if len(estudiantes)==0:
                print("Error, no hay estudiantes ingresados")
                time.sleep(2)
                continue
            else:
                print("**Agregar notas**")
                while True:
                    nombre = input("Nombre: ").strip().title()
                    if nombre in estudiantes:
                        try:
                            agregar_notas=float(input("Ingrese su nota: "))
                            if agregar_notas >=1.0 and agregar_notas <=7.0:
                                estudiantes[nombre].append(agregar_notas)
                                print(f"Nota agregada al estudiante {nombre}.")
                                time.sleep(2)
                                break
                            print("Error, la nota debe estar entre 1 y 7.")
                            time.sleep(2)
                        except ValueError:
                            print("Error, debe ingresar un número positivo")
                            time.sleep(2)
    elif opc=="3":
        if len(estudiantes)==0:
            print("No hay estudiantes registrados")
            time.sleep(2)
            continue
        else:
            print("**Mostrar lista de estudiantes**")
            for x in estudiantes:
                print(x,":",estudiantes[nombre_estudiante])
                time.sleep(2)
                break
    elif opc=="4":
        if len(estudiantes)==0:
            print("No hay estudiantes registrados")
            time.sleep(2)
            continue
        else:
            print("**Promedio de un estudiante**")

            promedio_estudiante=input("Ingrese el nombre: ")
            if promedio_estudiante not in estudiantes:
                print("Error, ese nombre no esta en la lista.")
                continue
            elif len(estudiantes[promedio_estudiante])==0:
                print("Error, el estudiante no tiene notas ingresadas")
                continue
            else: 
                    notas= sum(estudiantes[promedio_estudiante])/len(estudiantes[promedio_estudiante])
                    print(f"El promedio de {promedio_estudiante} es {notas}")
                    time.sleep(2)
                    continue
    elif opc=="5":
        print("**Promedio de los estudiantes**")
        if len(estudiantes)==0:
            print("No hay estudiantes registrados")
            time.sleep(2)
            continue
        else:
            for all_estudiantes in estudiantes:
                totales = sum(estudiantes[all_estudiantes]) / len(estudiantes[all_estudiantes])
                print(f"{all_estudiantes} > {totales}")    
                time.sleep(2)
                continue
    elif opc=="6":
        print("Gracias por usar el programa.")
        break
    else:
        print("Ingrese una opción correcta.")
        continue