lista=[]
for x in range (5):
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
suma_total=sum(lista)
promedio=suma_total/len(lista)        

print(f"Lista completa: {lista}")
print(f"La suma total: {suma_total}")
print(f"El promedio: {promedio}")