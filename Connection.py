import sys
from psycopg2 import pool

from logger_base import log

# Definicion de la clase
class Connection :
    # Atributos de clase
    _DB_NAME = 'py_test'
    _DB_USER = 'postgres'
    _DB_PASS = '8fi3Eo7l1'
    _DB_PORT = '5432'
    _DB_HOST = 'localhost'      # 127.0.0.1
    _MINIMUM = 1                #   Cantidad minima de conexiones
    _MAXIMUM = 4                #   Cantidad maxima de conexiones (Las bases de datos tienen limites para crear pools de acuerdo a los recursos)
    _pool    = None

    @classmethod
    def pool_exists( cls ) :
        return cls ._pool != None

    @classmethod
    def create_pool( cls ) :
        try:
            cls ._pool = pool .SimpleConnectionPool(
                cls ._MINIMUM,
                cls ._MAXIMUM,
                host = cls ._DB_HOST,
                user = cls ._DB_USER,
                password = cls ._DB_PASS,
                port = cls ._DB_PORT,
                database = cls ._DB_NAME
            )

            log .debug( f'Creacion exitosa del pool { cls ._pool }' )

            return cls ._pool
        except Exception as e:
            log .error( f'Error al obtener el pool: { e }' )
            sys .exit()

    @classmethod
    def get_pool( cls ) :
        if not cls .pool_exists() :

            return cls .create_pool()
        else :

            return cls ._pool

    @classmethod
    def get_pool_connection( cls ) :
        connection = cls .get_pool() .getconn()         #   Obtenemos un objeto de conexion del pool
        log .debug( f'Objeto de conexion obtenido del pool exitosamente { connection }' )

        return connection

    @classmethod
    def release_connection( cls, connection ) :
        cls .get_pool() .putconn( connection )          #   Libera un objeto de conexion y lo deja disponible en el pool de conexiones
        log .debug( f'Libera o regresa el objeto de conexion al pool { connection }' )

    @classmethod
    def close_connection( cls ) :
        cls .get_pool() .closeall()                     #   Cierra el pool de conexiones, es decir, cierra la conexion de todos los objetos de conexion del pool
        log .debug( 'Cierra el pool de conexiones' )


# ! Realizamos las respectivas pruebas a la clase
if __name__ == '__main__' :
    #   Solo podremos crear el numero maximo de conexiones que hemos espeficificado, 
    #   a no ser que dichos objetos se vayan liberando, en tal caso no se superara nunca
    #   el numero maximo establecido de objetos de conexion que puede tener el pool
    connection_1 = Connection .get_pool_connection()
    Connection .release_connection( connection_1 )

    connection_2 = Connection .get_pool_connection()

    connection_3 = Connection .get_pool_connection()
    Connection .release_connection( connection_3 )

    connection_4 = Connection .get_pool_connection()
    Connection .release_connection( connection_2 )
    Connection .release_connection( connection_4 )

    connection_5 = Connection .get_pool_connection()