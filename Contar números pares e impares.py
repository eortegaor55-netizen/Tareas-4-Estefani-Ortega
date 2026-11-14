"""Programa para contar cuantos números son pares y 
cuántos son impares en una lista de 10 número enteros
Autor: Estefani Ortega
Fecha: 14/11/2026
Descripción: Programa que lea 10 números enteros,  
los almacene en una lista y cuente cuántos números son pares y cuántos son impares"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Filtrar pares e impares
pares = [ n for n in numeros if n % 2 == 0]
impares = [ n for n in numeros if n % 2 !=0]

print(f"La cantidad de números pares es: {pares}")
print(f"La cantidad de números impares es: {impares}")
