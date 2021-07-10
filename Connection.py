import psycopg2 as db, sys

from logger_base import log

# Definicion de la clase
class Connection :
    # Atributos de clase
    _DB_NAME = 'py_test'
    _DB_USER = 'postgres'
    _DB_PASS = '8fi3Eo7l1'
    _DB_PORT = '5432'
    _DB_HOST = 'localhost'     # 127.0.0.1
    _connection = None
    _cursor = None

    @classmethod
    def is_connected( cls ) :
        return cls ._connection != None

    @classmethod
    def cursor_exists( cls ) :
        return cls ._cursor != None

    @classmethod
    def get_connection( cls ) :

        if not cls .is_connected() :

            return cls. create_connection()
        else :

            return cls. _connection

    @classmethod
    def create_connection( cls ) :
        try:
            #   Crea la conexión a la base de datos
            cls ._connection = db .connect(
                host = cls ._DB_HOST,
                user = cls ._DB_USER,
                password = cls ._DB_PASS,
                port = cls ._DB_PORT,
                database = cls ._DB_NAME
            )

            log .debug( f'Conexión a la BD exitosa { cls ._connection }' )                  #   Log: Lanza mensaje al terminal y almacena en el archivo de log de la aplicacion

            return cls ._connection
        except Exception as e:
            log .error( f'No se puede conectar a la BD: { e }' )                            #   Log: Lanza mensaje al terminal y almacena en el archivo de log de la aplicacion
            sys .exit()                                                                     #   Damos por terminado nuestro programa en el sistema

    @classmethod
    def get_cursor( cls ) :

        if not cls .cursor_exists() :

            return cls .create_cursor()
        else :

            return cls ._cursor

    @classmethod
    def create_cursor( cls ) :
        try:
            cls ._cursor = cls .get_connection() .cursor()                                  #   Obtiene la conexión a la base de datos y asigna el cursor
            log .debug( f'Se abrió correctamente el objeto cursor: { cls ._cursor }' )      #   Log: Lanza mensaje al terminal y almacena en el archivo de log de la aplicacion

            return cls ._cursor
        except Exception as e:
            log .error( f'No pudo crear el cursor: { e }' )                                 #   Log: Lanza mensaje al terminal y almacena en el archivo de log de la aplicacion
            sys .exit()                                                                     #   Damos por terminado nuestro programa en el sistema


# ! Realizamos las respectivas pruebas a la clase
if __name__ == '__main__' :
    Connection .get_connection()
    Connection .get_cursor()
