

libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True}]   

usuarios = ["megan"]      

archivados = []

prestamos = [
    {"usuario": "megan", "libro": "1984", "fecha": "2025-06-21"},]     

historial = []


def mostrar_catalogo():
    for libro in libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"{libro['titulo']} ({libro['autor']}) {estado}")
        
def prestar_libro(usuario, titulo, fecha):
    for libro in libros:
        if libro["titulo"] == titulo and libro["disponible"]:
            libro["disponible"] = False
            prestamos.append({"usuario": usuario, "libro": titulo, "fecha": fecha})
            historial.append(f"{usuario} presto el libro '{titulo}' el {fecha}")
            return
        
def buscar_libro(texto):
    return [libro for libro in libros if texto.lower() in libro["titulo"].lower()]

def agregar_usuario(nombre):
        for usuario in usuarios:
            if nombre not in usuarios:
                usuarios.append(nombre)
                historial.append(f"{nombre} se registro como usuario")
                
def agregar_libro(titulo, autor):
        libros.append({"titulo": titulo, "autor": autor, "disponible": True})

def eliminar_libro(titulo):
    global libros
    for libro in libros:
        if libro["titulo"] == titulo:
            archivados.append(libro) 
            libros.remove(libro)     
            return
    print("Se elimino el libro")


agregar_libro("La metamorfosis","Franz Kafka")

'''menu'''

while True:

    print(f"\n Elige una opcion.")
    print("1. Mostrar catalogo") 
    '''
    print("2. Contar equipos que ganaron en semifinales (SFI)")
    print("3. Contar partidos en cuartos de final (QFI) con más de 2 goles")
    print("4. Agregar más códigos")
    print("5. Ver códigos")
    print("6. Borrar todos los códigos")
    '''
    opcion = input("Elige una opción del 1 al 6. ")
    if opcion == "1":
        
            print(f"\n {mostrar_catalogo()}")

    '''elif opcion == "2":
        
        total_sfi = ganadores_semifinal(lista_codigos)
        print(f"Equipos que ganaron en semifinales: {total_sfi}")
        


    elif opcion == "3":
        
        total_cuartos_2goles = contar_part_goles_cuartos(lista_codigos)
        print(f"Partidos en cuartos de final con más de 2 goles: {total_cuartos_2goles}")
    

    elif opcion == "4":
        
        while True:
            nuevo = input("  Ingresa el código a agregar ")
            if not nuevo:
                break
            lista_codigos.append(nuevo)
            print("codigo agregado.")
            
    elif opcion == "5":

        if lista_codigos:
            print("Códigos actuales:")
            for i, codigo in enumerate(lista_codigos, start=1):
                print(f"  {i}. {codigo}")
        else:
            print("La lista esta vacía.")
            
    elif opcion == "6":
        
        lista_codigos.clear()
        print("Todos los códigos han sido borrados.")
        
    else:
        print("Elige una opcion valida")
        break'''

