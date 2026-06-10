notas = {

    "Pedro": 5.5,
    "María": 6.2,
    "Juan": 4.8,
    "Ana": 7.0
}
while True:
    nombres=input("Ingrese su nombre:").strip().title()
    if len(nombres) >= 3:
        print("Nombre válido")
        break
    print("Error el nombre debe ser más largo.")
    
if nombres in notas:
    nota= notas[nombres] 
    print(f"La nota de {nombres} es {nota}")
else:
    print("Alumno no encontrado")

if nota >=4:
    print("Aprobado")
else:
    print("Reprobado")