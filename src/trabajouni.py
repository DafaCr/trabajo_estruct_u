from queue import LifoQueue
from consolemenu import *
from consolemenu.items import *
from datetime import *
from tabulate import tabulate

libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True, "genero": "Realismo mágico", "ISBN": "978-7812345678", "id": 1, "sede": "San Miguel"},
    {"titulo": "1984", "autor": "George Orwell", "disponible": False, "genero": "Distopía", "ISBN": "978-7612345678", "id": 2, "sede": "San Isidro"},
    {"titulo": "Crimen y castigo", "autor": "Fiódor Dostoyevski", "disponible": True, "genero": "Ficción psicológica", "ISBN": "978-7512345678", "id": 3, "sede": "Monterrico"},
    {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "disponible": False, "genero": "Romance", "ISBN": "978-7412345678", "id": 4, "sede": "Villa"},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": True, "genero": "Literatura experimental", "ISBN": "978-7312345678", "id": 5, "sede": "San Miguel"},
    {"titulo": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "disponible": True, "genero": "Ficción", "ISBN": "978-7212345678", "id": 6, "sede": "San Isidro"},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "disponible": False, "genero": "Novela de caballería", "ISBN": "978-7112345678", "id": 7, "sede": "Monterrico"},
    {"titulo": "La Odisea", "autor": "Homero", "disponible": True, "genero": "Épica", "ISBN": "978-7012345678", "id": 8, "sede": "Villa"},
    {"titulo": "Matar a un ruiseñor", "autor": "Harper Lee", "disponible": False, "genero": "Ficción", "ISBN": "978-6912345678", "id": 9, "sede": "San Miguel"},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "disponible": True, "genero": "Ciencia ficción", "ISBN": "978-6812345678", "id": 10, "sede": "San Isidro"},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "disponible": True, "genero": "Romance", "ISBN": "978-6712345678", "id": 11, "sede": "Monterrico"},
    {"titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "disponible": False, "genero": "Ficción filosófica", "ISBN": "978-6612345678", "id": 12, "sede": "Villa"},
    {"titulo": "Los detectives salvajes", "autor": "Roberto Bolaño", "disponible": True, "genero": "Ficción", "ISBN": "978-6512345678", "id": 13, "sede": "San Miguel"},
    {"titulo": "El nombre de la rosa", "autor": "Umberto Eco", "disponible": True, "genero": "Misterio histórico", "ISBN": "978-6412345678", "id": 14, "sede": "San Isidro"},
    {"titulo": "El extranjero", "autor": "Albert Camus", "disponible": False, "genero": "Existencialismo", "ISBN": "978-6312345678", "id": 15, "sede": "Monterrico"},
    {"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "disponible": True, "genero": "Realismo mágico", "ISBN": "978-6212345678", "id": 16, "sede": "Villa"},
    {"titulo": "Los miserables", "autor": "Victor Hugo", "disponible": False, "genero": "Ficción histórica", "ISBN": "978-6112345678", "id": 17, "sede": "San Miguel"},
    {"titulo": "Viaje al centro de la Tierra", "autor": "Jules Verne", "disponible": True, "genero": "Aventura", "ISBN": "978-6012345678", "id": 18, "sede": "San Isidro"},
    {"titulo": "Cumbres borrascosas", "autor": "Emily Brontë", "disponible": False, "genero": "Romance gótico", "ISBN": "978-5912345678", "id": 19, "sede": "Monterrico"},
    {"titulo": "Frankenstein", "autor": "Mary Shelley", "disponible": True, "genero": "Ciencia ficción", "ISBN": "978-5812345678", "id": 20, "sede": "Villa"},
    {"titulo": "Matar a un ruiseñor", "autor": "Harper Lee", "disponible": True, "genero": "Ficción social", "ISBN": "978-5712345678", "id": 21, "sede": "San Isidro"},
    {"titulo": "1984", "autor": "George Orwell", "disponible": False, "genero": "Distopía", "ISBN": "978-5612345678", "id": 22, "sede": "San Miguel"},
    {"titulo": "Rebelión en la granja", "autor": "George Orwell", "disponible": True, "genero": "Sátira política", "ISBN": "978-5512345678", "id": 23, "sede": "Monterrico"},
    {"titulo": "El retrato de Dorian Gray", "autor": "Oscar Wilde", "disponible": True, "genero": "Ficción gótica", "ISBN": "978-5412345678", "id": 24, "sede": "Villa"},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "disponible": False, "genero": "Ciencia ficción", "ISBN": "978-5312345678", "id": 25, "sede": "San Miguel"},
    {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "disponible": True, "genero": "Realismo mágico", "ISBN": "978-5212345678", "id": 26, "sede": "San Isidro"},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "disponible": False, "genero": "Aventura", "ISBN": "978-5112345678", "id": 27, "sede": "Monterrico"},
    {"titulo": "El túnel", "autor": "Ernesto Sabato", "disponible": True, "genero": "Psicológico", "ISBN": "978-5012345678", "id": 28, "sede": "Villa"},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": True, "genero": "Narrativa experimental", "ISBN": "978-4912345678", "id": 29, "sede": "San Isidro"},
    {"titulo": "El Aleph", "autor": "Jorge Luis Borges", "disponible": False, "genero": "Fantasía", "ISBN": "978-4812345678", "id": 30, "sede": "San Isidro"},
    {"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "disponible": True, "genero": "Realismo mágico", "ISBN": "978-4712345678", "id": 31, "sede": "Monterrico"},
    {"titulo": "Los detectives salvajes", "autor": "Roberto Bolaño", "disponible": False, "genero": "Ficción", "ISBN": "978-4612345678", "id": 32, "sede": "Villa"},
    {"titulo": "2666", "autor": "Roberto Bolaño", "disponible": True, "genero": "Ficción literaria", "ISBN": "978-4512345678", "id": 33, "sede": "San Miguel"},
    {"titulo": "La tregua", "autor": "Mario Benedetti", "disponible": True, "genero": "Romance", "ISBN": "978-4412345678", "id": 34, "sede": "San Isidro"},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "disponible": False, "genero": "Romance", "ISBN": "978-4312345678", "id": 35, "sede": "Monterrico"},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "disponible": True, "genero": "Realismo mágico", "ISBN": "978-4212345678", "id": 36, "sede": "Villa"},
    {"titulo": "Como agua para chocolate", "autor": "Laura Esquivel", "disponible": True, "genero": "Romance mágico", "ISBN": "978-4112345678", "id": 37, "sede": "San Miguel"},
    {"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "disponible": False, "genero": "Misterio", "ISBN": "978-4012345678", "id": 38, "sede": "San Isidro"},
    {"titulo": "Marina", "autor": "Carlos Ruiz Zafón", "disponible": True, "genero": "Misterio juvenil", "ISBN": "978-3912345678", "id": 39, "sede": "Monterrico"},
    {"titulo": "El príncipe", "autor": "Nicolás Maquiavelo", "disponible": True, "genero": "Política", "ISBN": "978-3812345678", "id": 40, "sede": "Villa"}]

usuarios = [
    {"nombre": "Lucía", "apellido": "Ramírez", "id": 1, "sede": "San Miguel"},
    {"nombre": "Mateo", "apellido": "González", "id": 2, "sede": "San Isidro"},
    {"nombre": "Valentina", "apellido": "Fernández", "id": 3, "sede": "Monterrico"},
    {"nombre": "Santiago", "apellido": "Torres", "id": 4, "sede": "Villa"},
    {"nombre": "Isabella", "apellido": "Mendoza", "id": 5, "sede": "San Miguel"},
    {"nombre": "Emilia", "apellido": "Morales", "id": 6, "sede": "San Isidro"},
    {"nombre": "Benjamín", "apellido": "Castro", "id": 7, "sede": "Monterrico"},
    {"nombre": "Martina", "apellido": "Silva", "id": 8, "sede": "Villa"},
    {"nombre": "Thiago", "apellido": "Herrera", "id": 9, "sede": "San Miguel"},
    {"nombre": "Antonia", "apellido": "Cruz", "id": 10, "sede": "San Isidro"}
]

archivados = []

prestamos = [
    {"usuario": 1, "libro": 3, "fecha_inicio": "21-06-2025", "fecha_fin": "05-07-2025"},
    {"usuario": 2, "libro": 7, "fecha_inicio": "19-06-2025", "fecha_fin": "03-07-2025"},
    {"usuario": 3, "libro": 12, "fecha_inicio": "20-06-2025", "fecha_fin": "04-07-2025"},
    {"usuario": 4, "libro": 25, "fecha_inicio": "18-06-2025", "fecha_fin": "02-07-2025"},
    {"usuario": 5, "libro": 41, "fecha_inicio": "17-06-2025", "fecha_fin": "01-07-2025"},
    {"usuario": 2, "libro": 3, "fecha_inicio": "06-07-2025", "fecha_fin": "20-07-2025"},
    {"usuario": 4, "libro": 12, "fecha_inicio": "05-07-2025", "fecha_fin": "19-07-2025"},
    {"usuario": 6, "libro": 25, "fecha_inicio": "03-07-2025", "fecha_fin": "17-07-2025"},
    {"usuario": 8, "libro": 41, "fecha_inicio": "02-07-2025", "fecha_fin": "16-07-2025"},
    {"usuario": 10, "libro": 7, "fecha_inicio": "04-07-2025", "fecha_fin": "18-07-2025"},
    {"usuario": 3, "libro": 1, "fecha_inicio": "10-05-2025", "fecha_fin": "24-05-2025"},
    {"usuario": 6, "libro": 9, "fecha_inicio": "15-05-2025", "fecha_fin": "29-05-2025"},
    {"usuario": 9, "libro": 22, "fecha_inicio": "20-05-2025", "fecha_fin": "03-06-2025"},
    {"usuario": 6, "libro": 4, "fecha_inicio": "05-05-2025", "fecha_fin": "19-05-2025"},
    {"usuario": 2, "libro": 4, "fecha_inicio": "20-05-2025", "fecha_fin": "03-06-2025"},
    {"usuario": 7, "libro": 4, "fecha_inicio": "04-06-2025", "fecha_fin": "18-06-2025"},
    {"usuario": 1, "libro": 4, "fecha_inicio": "19-06-2025", "fecha_fin": "03-07-2025"},
    {"usuario": 8, "libro": 4, "fecha_inicio": "04-07-2025", "fecha_fin": "18-07-2025"},
    {"usuario": 5, "libro": 4, "fecha_inicio": "19-07-2025", "fecha_fin": "02-08-2025"},
]

historial = []
sedes = ["San Isidro", "Villa", "San Miguel", "Monterrico"]
sedeActual = sedes[0]

def cambiar_sede():
    global sedeActual
    print("Sedes")
    print("1 - San Isidro")
    print("2 - Villa")
    print("3 - San Miguel")
    print("4 - Monterrico")
    nuevaSede = input("\nEscoger sede: ")
    sedeActual = sedes[int(nuevaSede) - 1]
    print("\nSede actual: " + sedeActual)
cambiar_sede()

subtitle = "Buscando desde la sede " + sedeActual
menu = ConsoleMenu("Biblioteca Zeus", subtitle)

def mostrar_catalogo():
    print("\nCatálogo de libros disponibles en la sede " + sedeActual + ":\n")
    tabla = []
    for libro in libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        if libro["sede"] == sedeActual:
            fila = [libro["id"], libro["titulo"], libro["autor"], estado]
            tabla.append(fila)

    encabezados = ["ID", "Título", "Autor", "Estado"]
    print(tabulate(tabla, headers=encabezados))
    input("\nPresiona Enter para continuar...")

def prestar_libro(titulo):
    usuario = input('Usuario: ')
    hoy = date.today()
    fecha_hoy_str = hoy.strftime("%d-%m-%Y")
    fecha_dos_semanas = hoy + timedelta(days=14)
    fecha_dos_semanas_str = fecha_dos_semanas.strftime("%d-%m-%Y")
    existe = False
    for libro in libros:
        if libro["titulo"] == titulo and libro["disponible"]:
            existe = True
            if libro["sede"] == sedeActual:
                libro["disponible"] = False
                prestamos.append({"usuario": usuario, "libro": titulo, "fecha_inicio": fecha_hoy_str, "fecha_fin": fecha_dos_semanas_str})
                historial.append(f"{usuario} presto el libro '{titulo}' el {fecha_hoy_str}. Fecha de devolución: {fecha_dos_semanas_str}")
                print(historial[-1])
                input("\nPresiona Enter para continuar...")
                return
            elif libro["sede"] != sedeActual:
                print("Este es un préstamo intersedes, la fecha de inicio es el lunes próximo")
                dias_hasta_lunes = (7 - hoy.weekday()) % 7
                dias_hasta_lunes = 7 if dias_hasta_lunes == 0 else dias_hasta_lunes
                lunes = hoy + timedelta(days=dias_hasta_lunes)
                prox_lunes = lunes.strftime("%d-%m-%Y")
                fecha_dos_sem_desde_lunes = lunes + timedelta(days=14)
                fecha_dos_sem_desde_lunes_str = fecha_dos_sem_desde_lunes.strftime("%d-%m-%Y")
                libro["disponible"] = False
                prestamos.append({"usuario": usuario, "libro": titulo, "fecha_inicio": prox_lunes, "fecha_fin": fecha_dos_sem_desde_lunes_str})
                historial.append(f"{usuario} solicitó préstamo intersedes del libro '{titulo}' el {fecha_hoy_str}. Fecha de devolución: {fecha_dos_sem_desde_lunes_str}")
                print(historial[-1])
                input("\nPresiona Enter para continuar...")
                return
    
    if existe == False:
        print("Ese libro no está disponible")
        input("\nPresiona Enter para continuar...")
        
def prestar_libro_outer():
    titulo = input('Título: ')
    prestar_libro(titulo)

def prestar_libro_entre_sedes(titulo):
    usuario = input('Usuario: ')
    hoy = date.today()
    fecha_hoy_str = hoy.strftime("%d-%m-%Y")
    fecha_dos_semanas = hoy + timedelta(days=14)
    fecha_dos_semanas_str = fecha_dos_semanas.strftime("%d-%m-%Y")
    for libro in libros:
        if libro["titulo"] == titulo and libro["disponible"]:
            libro["disponible"] = False
            prestamos.append({"usuario": usuario, "libro": titulo, "fecha_inicio": fecha_hoy_str, "fecha_fin": fecha_dos_semanas_str})
            historial.append(f"{usuario} presto el libro '{titulo}' el {fecha_hoy_str}")
            return

def buscar_libro():
    texto = input('Buscar título: ')
    resultados = []

    for libro in libros:
        if texto.lower() in libro["titulo"].lower() and libro["disponible"]:
            fila = [libro["titulo"], libro["autor"], libro["sede"]]
            resultados.append(fila)
    
    if resultados:
        print("\nLibros disponibles en tu sede:")
        print(tabulate(resultados, headers=["Título", "Autor", "Sede"], tablefmt="fancy_grid"))
    else:
        print("\nNo hay copias disponibles de '" + texto + "'.")
    input("\nPresiona Enter para continuar...")

def eliminar_libro():
    titulo = input('Título: ')
    global libros
    existe = False
    for libro in libros:
        if libro["titulo"] == titulo and libro["disponible"]:
            existe = True
            archivados.append(libro)
            libros.remove(libro)
            historial.append(f"se archivó el libro '{titulo}'")
            print(historial[-1])
            input("\nPresiona Enter para continuar...")
            return
        elif libro["titulo"] == titulo and libro["disponible"] == False:
            existe = True
            print("Este libro no se puede archivar porque está en un préstamo activo.")
            input("\nPresiona Enter para continuar...")
            return
    
    if existe == False:
        print("Este libro no existe.")
        input("\nPresiona Enter para continuar...")

def devolver_libro():
    titulo = input('Título: ')
    usuario = input('Usuario: ')
    for libro in libros:
        if libro["titulo"] == titulo:
            libro["disponible"] = True
            historial.append(f"{usuario} devolvió el libro '{titulo}'")
            print(historial[-1])
            input("\nPresiona Enter para continuar...")
            return

def intercambio(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def libros_mas_prestados():
    conteo = {}

    for prestamo in prestamos:
        id_libro = prestamo["libro"]
        titulo = next((libro["titulo"] for libro in libros if libro["id"] == id_libro), None)

        if titulo:
            if titulo in conteo:
                conteo[titulo] += 1
            else:
                conteo[titulo] = 1

    # Convertir a lista de tuplas
    lista_conteo = list(conteo.items())

    ordenamientoInsercion(lista_conteo)

    headers = ["Título del Libro", "Cantidad de Préstamos"]
    print("\n📚 Libros más prestados:\n")
    print(tabulate(lista_conteo, headers=headers))
    input("\nPresiona Enter para continuar...")

def ordenamientoInsercion(lista):
    for i in range(1, len(lista)):
        pos = i
        while pos > 0 and lista[pos][1] > lista[pos - 1][1]:
            intercambio(lista, pos, pos - 1)
            pos -= 1

def intercambio(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def mostrar_historial():
    print("Historial de Actividades:")
    for accion in historial:
        print("- " + accion)
    input("\nPresiona Enter para continuar...")

tramite = LifoQueue()

def ordenar ():
    global tramite
    if not tramite.empty():
        data = tramite.get()
        titulo = data["titulo"]
        usuario = data["usuario"]
        
        for libro in libros:
            if libro["titulo"] == titulo:   
                libro["disponible"] = True
                historial.append(f"{usuario} devolvió el libro '{titulo}'")    

function_item = FunctionItem('Mostrar catálogo', mostrar_catalogo)
function_item1 = FunctionItem('Pedir libro prestado', prestar_libro_outer)
function_item2 = FunctionItem('Devolver libro', devolver_libro)
function_item3 = FunctionItem('Buscar libro', buscar_libro)
function_item4 = FunctionItem('Eliminar libro', eliminar_libro)
function_item5 = FunctionItem('Ver historial', mostrar_historial)
function_item6 = FunctionItem('Obtener análisis de popularidad', libros_mas_prestados)
menu.append_item(function_item)
menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(function_item4)
menu.append_item(function_item5)
menu.append_item(function_item6)

menu.show()