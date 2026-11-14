""" Programa de ordenamiento burbuja
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Programa que pide al usuario la cantidad de elementos 
solicita cada número, los almacena en una lista e implementa
el método de burbuja para ordenarlos de mayor a menor"""

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista

elementos = input("Ingrese los números separados por comas que quiere ordenar: ")
numeros = [int(x) for x in elementos.split(",")]
ordenados = ordenamiento_burbuja(numeros)
print("Lista ordenada:", ordenados)
