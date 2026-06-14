lista=[]
def agregar_numeros():
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

def suma_lista():
    suma_total=sum(lista)
    print(f"La suma total: {suma_total}")
    return suma_total

def promedio_lista():
    promedio=suma/len(lista)
    print(f"Promedio de la lista: {promedio}")

def largo_lista():
    print(f"El largo de la lista es: {len(lista)}")

for x in range (5):
    num=agregar_numeros()

suma=suma_lista()
promedio=promedio_lista()
largo_lista=largo_lista()

    