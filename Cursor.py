from logger_base import log

from Connection import Connection

# Definicion de la clase para el cursor del pool
class Cursor :

    def __init__( self ) :
        self ._connection = None
        self ._cursor = None

    #   __enter__ (Dunder): Obtiene una conexion cuando se use el bloque with (Resolve Manager)
    def __enter__( self ) :
        log .debug( f'with (__enter__): Obtiene objeto de conexion' )
        self ._connection = Connection .get_pool_connection()       #   Obtenemos un objeto de conexion del pool
        self ._cursor = self ._connection .cursor()                 #   Obtenemos el cursor del respectivo objeto de conexion

        return self ._cursor

    #   __exit__ (Dunder): Cuando finalice bloque with (Resolve Manager). Se encargara de: 1.) Hacer el commit o el rollback de la transaccion 2.) Regresar el objeto de conexion al pool
    def __exit__( self, exception_type, exception_value, exception_traceback ) :
        log .debug( f'with (__exit__): Realiza commit o rollback y libera objeto de conexion' )

        #   Verifica si existe una excepcion
        if exception_value :
            self ._connection .rollback()           #   Se reestablecen los cambios de todos los Queries realizados sobre la base de datos
            log .error( f'Ocurrio una excepcion (Rollback) { exception_value } { exception_type } { exception_traceback }' )

        else :
            self ._connection .commit()             #   Se guardan los cambios de todos los Queries realizados sobre la base de datos
            log .debug( 'Guarda cambios DB (Commit)' )

        self ._cursor .close()                                  #   Cerramos el cursor
        Connection .release_connection( self ._connection )     #   Libera un objeto de conexion y lo deja disponible en el pool de conexiones


# ! Realizamos las respectivas pruebas a la clase
if __name__ == '__main__' :
    with Cursor() as cursor :
        # Dentro de este bloque se pueden hacer todo tipo de operaciones CRUD a la BD
        query = 'SELECT * FROM people'
        log .debug( f'Ejecuta Query: { query }' )

        cursor .execute( query )                #   Ejecuta el query
        log .debug( cursor .fetchall() )        #   Recupera registros
