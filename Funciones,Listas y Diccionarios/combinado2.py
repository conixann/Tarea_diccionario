import os,time
def pedir_nombre():
    while True:
        nombre=input("Ingrese el nombre: ").strip().title()
        
        tiene_numero = False
        for letra in nombre:
            if letra.isdigit():
                tiene_numero= True

        if len(nombre) < 3:
            print("Error")
        elif tiene_numero:
            print("Error")
        else:
            return nombre
        
def pedir_num():

    while True:
        try:
            telefono=input("Ingrese el número de telefono (569): ").strip().title()
            if len(telefono)==8:
                return telefono
            print("Error, el número debe contener 8 cáracteres.")
        except ValueError:
            print("Error debes ingresar un número entero positivo")

agenda=[]
os.system('cls')
for x in range(3):
    nombres=pedir_nombre()
    telefonos=pedir_num()
    contacto={
        "nombre":nombres,
        "telefono":telefonos,
    }
    agenda.append(contacto)

for x in agenda:
    print(x["nombre"], ">>", x["telefono"])

