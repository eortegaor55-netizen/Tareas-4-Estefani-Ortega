""" Programa agregar contactos
Autora: Estefani Ortega
Fecha: 14/11/2026
Descripción: Programa para crear una lista de diccionarios que 
represente una agenda de contactos (nombre, telefono, email) implementar
funciones para agregar un contacto, busca un contacto por nombre,
eliminar un contato y lista de todos los contactos"""

contactos = [
    {
        "nombre": "Ana García",
        "telefono": "555-1234",
        "email": "ana.garcia@gmail.com",
    },
    {
        "nombre": "Carlos López",
        "telefono": "555-5678",
        "email": "carlos.lopez@gmail.com",
    },
]

# 2. Función para agregar un contacto
def agregar_contacto(lista_contactos, nombre, telefono, email):
    nuevo_contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    lista_contactos.append(nuevo_contacto)
    print(f"Contacto '{nombre}' agregado correctamente.")


# 3. Función para buscar un contacto por nombre
def buscar_contacto(lista_contactos, nombre_buscar):
    encontrados = [
        c
        for c in lista_contactos
        if nombre_buscar.lower() in c["nombre"].lower()
    ]

    if encontrados:
        print(f"\n--- Resultados para '{nombre_buscar}' ---")
        for c in encontrados:
            print(
                f"Nombre: {c['nombre']} | Teléfono: {c['telefono']} | Email:"
                f" {c['email']}"
            )
    else:
        print(f"\nNo se encontró ningún contacto con el nombre '{nombre_buscar}'.")


# 4. Función para eliminar un contacto por nombre exacto
def eliminar_contacto(lista_contactos, nombre_eliminar):
    for i, contacto in enumerate(lista_contactos):
        if contacto["nombre"].lower() == nombre_eliminar.lower():
            eliminado = lista_contactos.pop(i)
            print(f"\nContacto '{eliminado['nombre']}' eliminado.")
            return
    print(f"\nNo se pudo eliminar: '{nombre_eliminar}' no existe en la agenda.")


# 5. Función para listar todos los contactos
def listar_contactos(lista_contactos):
    print("\n--- Lista de Contactos ---")
    if not lista_contactos:
        print("La agenda está vacía.")
        return

    for i, c in enumerate(lista_contactos, start=1):
        print(
            f"{i}. Nombre: {c['nombre']} | Teléfono: {c['telefono']} | Email:"
            f" {c['email']}"
        )

listar_contactos(contactos)

agregar_contacto(contactos, "María Pérez", "555-9876", "maria.perez@email.com")
buscar_contacto(contactos, "Ana")
eliminar_contacto(contactos, "Carlos López")

listar_contactos(contactos)