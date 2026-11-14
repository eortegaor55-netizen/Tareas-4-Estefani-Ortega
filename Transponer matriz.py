""" Programa para transponer una matriz
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Desarrolla un programa que lea una 
matriz de 3x3 y calcule la transpuesta"""

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

#Transponer la matriz

transpuesta = []
for j in range(len(matriz[0])):
    fila_nueva = []
    for i in range(len(matriz)):
        fila_nueva.append(matriz[i][j])
    transpuesta.append(fila_nueva)
print(matriz)
print(transpuesta)
  