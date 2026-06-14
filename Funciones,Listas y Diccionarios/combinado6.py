lista=[]

def ingresa_numero():
     while True:
        try:
            num=int(input("Ingrese un número: "))
            if num > 0:
                lista.append(num)
                print("Número guardado exitosamente")
                return num
            print("El número debe ser mayor a 0")
        except ValueError:
            print("Ingrese un número entero positivo.")

def definir_num():

    mayor=lista[0]
    menor=lista[0]


    for numero in lista:
        if numero > mayor:
            mayor = numero

        if numero < menor: 
            menor = numero 
    print("Número mayor:", mayor)
    print("Número menor:", menor)
                

def cantidad_num():
    print("Cantidad de números:", len(lista))


for x in range (8):
    num=ingresa_numero()

definir=definir_num()
cantidad_num()
