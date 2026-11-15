""" Programa Catálogo de películas
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Programa para crear un catálogo de películas"""


catalogo_peliculas = [
    {
        "titulo": "Inception",
        "director": "Christopher Nolan",
        "anio": 2010,
        "genero": "Ciencia Ficción",
        "duracion": 148
    },
    {
        "titulo": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "anio": 1994,
        "genero": "Crimen",
        "duracion": 154
    },
    {
        "titulo": "Interstellar",
        "director": "Christopher Nolan",
        "anio": 2014,
        "genero": "Ciencia Ficción",
        "duracion": 169
    },
    {
        "titulo": "Toy Story",
        "director": "John Lasseter",
        "anio": 1995,
        "genero": "Animación",
        "duracion": 81
    }
]

# 2. Función para filtrar por género
def filtrar_por_genero(catalogo, genero):
    return [
        pelicula for pelicula in catalogo 
        if pelicula["genero"].lower() == genero.lower()
    ]

#  filtrar películas estrenadas después de cierto año
def filtrar_despues_de_anio(catalogo, anio_limite):
    return [
        pelicula for pelicula in catalogo 
        if pelicula["anio"] > anio_limite
    ]

# ordenar por duración (ascendente por defecto)
def ordenar_por_duracion(catalogo, descendente=False):
    return sorted(
        catalogo, 
        key=lambda pelicula: pelicula["duracion"], 
        reverse=descendente
    )

# calcular la duración promedio
def calcular_duracion_promedio(catalogo):
    if not catalogo:
        return 0
    total_minutos = sum(pelicula["duracion"] for pelicula in catalogo)
    return round(total_minutos / len(catalogo), 2)

if __name__ == "__main__":
    print("--- Películas de Ciencia Ficción ---")
    for p in filtrar_por_genero(catalogo_peliculas, "Ciencia Ficción"):
        print(f"- {p['titulo']} ({p['anio']})")

    print("\n--- Películas estrenadas después del 2000 ---")
    for p in filtrar_despues_de_anio(catalogo_peliculas, 2000):
        print(f"- {p['titulo']} ({p['anio']})")

    print("\n--- Ordenadas por duración (Mayor a menor) ---")
    for p in ordenar_por_duracion(catalogo_peliculas, descendente=True):
        print(f"- {p['titulo']}: {p['duracion']} min")

    promedio = calcular_duracion_promedio(catalogo_peliculas)
    print(f"\n--- Duración promedio del catálogo: {promedio} minutos ---")
