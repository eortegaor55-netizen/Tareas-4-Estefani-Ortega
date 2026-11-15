""" Programa Inventario de productos
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Programa para crear un inventario de productos, donde cada 
clave sea el código del producto y el valor
otro diccionario con nombre, precio y stock
Los productos con stock bajo (menos de 5 unidades)"""

inventario = {
    "P1": {"nombre": "Computadora", "precio": 850.00, "stock": 12},
    "P2": {"nombre": "Mouse", "precio": 320.50, "stock": 3},
    "P3": {"nombre": "Monitor", "precio": 3200.00, "stock": 2},
}

# 2. Filtrar y mostrar los productos con stock bajo (menos de 5 unidades)
print("productos con stock bajo (Menos de 5 unidades):")
print("-" * 50)

for codigo, datos in inventario.items():
    if datos["stock"] < 5:
        print(f"Código: {codigo} | Producto: {datos['nombre']} | Stock: {datos['stock']} uds.")
