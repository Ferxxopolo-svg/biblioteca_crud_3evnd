from dao.libro_dao import LibroDAO
from models.libros import Libro

def ver_todo(libro_dao):
    try:
        
        libros = libro_dao.obtener_libros()

        print("Libros en la biblioteca")
        if len(libros) == 0:
            print("No hay libros en la biblioteca")
        else :
            for libro in libros:
                print(f"{libro.titulo} - {libro.autor} - {libro.disponible}")

        print("\n Conexion exitosa a la base de datos")

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def insertar_libro(libro_dao):
    try:
        print("--------------------------------------")
        print("Inserción de un nuevo libro")
        titulo = input("Escribe el título del libro: ")
        autor = int(input("Escibre el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True
        nuevoLibro = Libro(8,titulo,autor,disponible)
        libro_dao.insertar(nuevoLibro)
    except Exception as e:
        print(f"Error al insertar libro: {e}")

def actualizar_libro(libro_dao):
    ver_todo(libro_dao)
    id = int(input("Escribe el id del libro a editar: "))
    print("Actualiza los datos de este libro")
    titulo = input("Escribe el nuevo titulo del libro: ")
    autor = input("Escribe el nuevo id del autor: ")
    isbn = input("Escribe el nuevo isbn del libro: ")
    disponible = bool(input("Escribe si el libro esta disponible o no"))
    libro = Libro(id, titulo, autor, isbn, disponible)
    libro_dao.actualizar(libro)

def eliminar_libro(libro_dao):
    ver_todo(libro_dao)
    id = int(input("Escribe el id del libro a eliminar: "))
    libro_dao.eliminar(id)
    print("Libros Disponibles")
    ver_todo(libro_dao)

def main():
    print("=== Biblioteca Universitaria ==")
    libro_dao = LibroDAO()

    # Imprime el menú de opciones
    print("1. Ver todos los libros")
    print("2. Insertar nuevo libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")

    opcion = int(input("Escribe una opcion (1-4): "))

    match opcion:
        case 1:ver_todo(libro_dao)
        case 2:insertar_libro(libro_dao)
        case 3:actualizar_libro(libro_dao)
        case 4:eliminar_libro(libro_dao)

if __name__ == "__main__":
    main()