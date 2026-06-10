agenda=[]

for x in range (3):
    while True:
        nombres=input(f"Ingrese el nombre {x+1}:")
        if len(nombres) >= 3:
            print("Nombre válido")
            break
        print("Error, el nombre debe ser más largo")
    while True:
        try:
            telefono=int(input(f"Ingrese el número de telefono {x+1} (569): "))
            if len(telefono) == 8:
                print("Número válido")
                break
            print("Error, el número debe contener 8 caracteres")
        except ValueError:
            print("Ingrese un número entero positivo")

            contacto = {
                "nombre":nombres,
                "telefono":telefono,
            }
            agenda.append(contacto)
for x in agenda:
    print(x["nombre"], ">", x["telefono"])