# DAO: Data Access Object
# Es una clase que se encarga acceder a la base de datos y realizar las operaciones

from database.conexion import conexion
from models.libros import Libro

class LibroDAO:

    # Select * from libros
    def obtener_libros(self):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libros")

        registros = cursor.fetchall() 

        libros = []
        for registro in registros:
            libro = Libro(id=registro[0], titulo=registro[1], autor=registro[2], isbn=registro[3], disponible=registro[4])
            libros.append(libro)

        cursor.close()
        conexion.close()
        return libros
    
# Insert
    def agregar_libro(self, libro):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO libros (titulo, autor, isbn, disponible)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (libro.titulo, libro.autor, libro.isbn, libro.disponible))

        conexion.commit()
        cursor.close()
        conexion.close()

# Update
    def actualizar(self, libro):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE libros
        SET titulo = %s, autor = %s, isbn = %s, disponible = %s
        WHERE id = %s
        """

        cursor.execute(sql, (libro.titulo, libro.autor, libro.isbn, libro.disponible, libro.id))

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM libro WHERE id = %s", (id,))
        conexion.commit()
        cursor.close()
        conexion.close()