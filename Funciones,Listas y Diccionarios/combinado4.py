import os,time
inventario= {
    "Laptop":10,
    "Mouse":25,
    "Teclado":15,
}

def mostrar_productos():
    print("Productos disponibles:")
    for producto, stock in inventario.items():
        print(f"{producto} > {stock}")

def solicitud_productos():
    while True:
        solicitud=input("¿Qué producto desea?:").strip().title()
        if solicitud in inventario:
            print(f"El producto {solicitud} encontrado, stock disponible {inventario[solicitud]}")
            return solicitud
        print("Porfavor reintente e ingrese un producto válido.")

def unidades_deseadas():
    while True:
        try:
            unidades=int(input("¿Cúantas unidades desea?:"))
            if unidades > 0:
                stock_disponible= inventario[solicitud_productos]
                if stock_disponible < unidades:
                    print("No hay stock suficiente.")
                    continue
                else:
                    nuevo_stock = stock_disponible - unidades
                    print(f"""Venta realizada! 
                            Cantidad actualizada {solicitud_productos} > {nuevo_stock}""")
                    return nuevo_stock
            print("Las unidades deben ser mayor que 0")
        except ValueError:
                print("Ingrese un número válido.")

os.system('cls')
mostrar_productos()

solicitud_productos=solicitud_productos()
stock=unidades_deseadas()