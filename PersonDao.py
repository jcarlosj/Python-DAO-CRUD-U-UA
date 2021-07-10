from logger_base import log
from Connection import Connection
from Person import Person

# Definicion de la clase
class PersonDao:
    '''
        DAO, (Data Access Object): Es un patrón de diseño que crea una capa para comunicarse con la base de datos
        CRUD, (Create, Read, Update, Delete): Operaciones que podemos realizar contra un motor de bases de datos
    '''
    # ! Atributos de Clase
    _SELECT = 'SELECT * FROM people ORDER BY id'
    _INSERT = 'INSERT INTO people( first_name, last_name, email ) VALUES ( %s, %s, %s )'
    _UPDATE = 'UPDATE people SET first_name=%s, last_name=%s, email=%s WHERE id=%s'
    _DELETE = 'DELETE FROM people WHERE id=%s'

    @classmethod
    def select( cls ) :

        with Connection .get_cursor() as cursor :
            people = []

            cursor .execute( cls ._SELECT )
            records = cursor .fetchall()

            for record in records :
                person = Person( record[ 0 ], record[ 1 ], record[ 2 ], record[ 3 ] )
                people .append( person )

            return people

# ! Realizamos las respectivas pruebas a la clase
if __name__ == '__main__' :
    people = PersonDao .select()
    for person in people :
        log .debug( person )