lista=[]
mayor=lista[0]
menor=lista[0]
for x in range (8):
    while True:
        try:
            num=int(input(f"{x+1}. Ingrese un número: "))
            if num > 0:
                lista.append(num)
                print("Número guardado exitosamente")
                break
            print("El número debe ser mayor a 0")
        except ValueError:
            print("Ingrese un número entero positivo.")

for numero in lista:
    if numero > mayor:
        mayor = numero

    if numero < menor: 
        menor = numero

print("Número mayor:", mayor)
print("Número menor:", menor)
print("Cantidad de números:", len(lista))