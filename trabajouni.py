

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
                
