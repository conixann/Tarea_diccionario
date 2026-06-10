inventario= {
    "Laptop":10,
    "Mouse":25,
    "Teclado":15,
}
print("Productos disponibles:")
for producto, stock in inventario.items():
    print(f"{producto} > {stock}")
while True:
    solicitud=input("¿Qué producto desea?:").strip().title()
    if solicitud in inventario:
        print(f"El producto {solicitud} encontrado, stock disponible {inventario[solicitud]}")
        break
    print("Porfavor reintente e ingrese un producto válido.")
while True:
    try:
        unidades=int(input("¿Cúantas unidades desea?:"))
        if unidades > 0:
            stock_disponible= inventario[solicitud]
            if stock_disponible < unidades:
                print("No hay stock suficiente.")
                continue
            else:
                nuevo_stock = stock_disponible - unidades
                print("Stock disponible!")
                break
        print("Las unidades deben ser mayor que 0")
    except ValueError:
        print("Ingrese un número válido.")