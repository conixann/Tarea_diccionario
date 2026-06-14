import os,time
def pedir_nombre(): 
    while True:
        nombres=input("Ingrese su nombre:").strip().title()
        if nombres in notas:
            if len(nombres) >= 3:
                print("Nombre válido")
                return nombres
            print("Error el nombre debe ser más largo.")
        print("El nombre no se encuentra registrado.")
def pedir_nota():
    if nombre in notas:
        nota= notas[nombre] 
        print(f"La nota de {nombre} es {nota}")
        return nota
    else:
        print("Alumno no encontrado")
        return None

def mostrar_estado(nota):
    if nota >=4:
        print("Aprobado")
        return nota
    else:
        print("Reprobado")
    
notas = {

    "Pedro": 5.5,
    "María": 6.2,
    "Juan": 4.8,
    "Ana": 7.0
}
os.system('cls')
nombre=pedir_nombre()
notas=pedir_nota()
estado=mostrar_estado(notas)