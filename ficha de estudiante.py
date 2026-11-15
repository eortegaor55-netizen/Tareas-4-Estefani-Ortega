""" Programa Ficha de estudiante
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Programa que solicita los datos de un estudiante
(nombrem edad, carrera, promedio) y los almacene en un 
diccionario. Luego muesta la ficha"""

def crear_ficha_estudiante(nombre, edad, carrera, promedio):
    return {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera, 
        "promedio": promedio
    }
def mostra_ficha_estudiante(estudiante):
    """ Muestra la ficha del estudiante """
    print("="*30)
    print(f"nombre:{estudiante['nombre']}")
    print(f"edad:{estudiante['edad']}")
    print(f"carrera:{estudiante['carrera']}")
    print(f"promedio:{estudiante['promedio']}")
if __name__ == "__main__":
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    carrera = input("Ingrese la carrera del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))

    estudiante = crear_ficha_estudiante(nombre, edad, carrera, promedio)
    mostra_ficha_estudiante(estudiante)