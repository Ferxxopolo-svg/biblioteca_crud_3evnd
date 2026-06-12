import psycopg2

class conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
            host="localhost",
            database="biblioteca3aevnd",
            user="postgres",
            password="donanfermc"
            port="5432"
        )
