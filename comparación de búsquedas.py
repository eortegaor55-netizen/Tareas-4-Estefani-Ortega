""" Programa comparación de búsquedas
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Programa qBusca un número con búsqueda lineal y con búsqueda binaria. Cuenta cuántas comparaciones 
ealiza cada algoritmo y muestra los resultados. 
Explica en un comentario por qué la búsqueda binaria es más eficiente."""


import random

# 1. Generar una lista de 1000 números aleatorios entre 1 y 10000, y ordenarla
numeros = sorted(random.sample(range(1, 10001), 1000))

# Elegir un número al azar dentro de la lista para garantizar que exista
objetivo = random.choice(numeros)

def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for indice, elemento in enumerate(lista):
        comparaciones += 1
        if elemento == objetivo:
            return indice, comparaciones
    return -1, comparaciones

def busqueda_binaria(lista, objetivo):
    comparaciones = 0
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        
        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return -1, comparaciones

# 2. Ejecutar ambos algoritmos
indice_lineal, comp_lineal = busqueda_lineal(numeros, objetivo)
indice_binaria, comp_binaria = busqueda_binaria(numeros, objetivo)

# 3. Mostrar los resultados
print(f"Número buscado: {objetivo}")
print(f"Búsqueda Lineal  -> Índice encontrado: {indice_lineal} | Comparaciones: {comp_lineal}")
print(f"Búsqueda Binaria -> Índice encontrado: {indice_binaria} | Comparaciones: {comp_binaria}")

# La búsqueda binaria es mucho más eficiente que la lineal en listas ordenadas
# porque compara el objetivo con el elemento central y descarta la mitad de los elementos
 # restantes, logrando una complejidad temporal logarítmica O(log n).
