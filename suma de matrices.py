"""Programa para sumar matrices
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Desarrolla un programa que lea 2 matrices de 2x2
(cuatro números cada una)almacene en una lista y calcule la suma
de ambas matrices"""

matriz1= [
    [3, 5],
    [7, 9]
]

matriz2= [
    [56, 30],
    [12, 10]
]
  
#Calcular la suma de ambas matrices
suma = 0 
for fila in matriz1:
    for elemento in fila:
        suma += elemento
for fila in matriz2:
    for elemento in fila:
        suma += elemento
        
print(f"La suma de los elementos de ambas matrices es: {suma}")
