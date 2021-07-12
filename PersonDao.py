from logger_base import log
from Person import Person
from Cursor import Cursor

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

        with Cursor() as cursor :
            people = []

            cursor .execute( cls ._SELECT )
            records = cursor .fetchall()

            for record in records :
                person = Person( record[ 0 ], record[ 1 ], record[ 2 ], record[ 3 ] )
                people .append( person )

            return people

    @classmethod
    def insert( cls, person ) :

        with Cursor() as cursor :

            values = ( person .first_name, person .last_name, person .email )       #   Creamos una tupla de los campos que vamos a insertar
            cursor .execute( cls ._INSERT, values )
            log .debug( f'Inserto: { person }' )                                    #   Debe estar activado en nivel debug para que este mensaje se visualice

            return cursor .rowcount                                                 #   Retorna numero de registros insertados

    @classmethod
    def update( cls, person ) :

        with Cursor() as cursor :

            values = ( person .first_name, person .last_name, person .email, person .id )   #   Creamos una tupla de los campos que vamos a insertar
            cursor .execute( cls ._UPDATE, values )
            log .debug( f'Actualizo: { person }' )                                  #   Debe estar activado en nivel debug para que este mensaje se visualice

            return cursor .rowcount                                                 #   Retorna numero de registros modificados

    @classmethod
    def delete( cls, person ) :

        with Cursor() as cursor :

            values = ( person .id, )                                                # Ponemos una coma (,) para que sea considerada como una tupla de un elemento
            cursor .execute( cls ._DELETE, values )
            log .debug( f'Elimino: { person }' )                                    #   Debe estar activado en nivel debug para que este mensaje se visualice

            return cursor .rowcount                                                 #   Retorna numero de registros modificados


# ! Realizamos las respectivas pruebas a la clase
if __name__ == '__main__' :

    # ? Insertar un nuevo registro
    # person_1 = Person( fname = 'German', lname = 'Jimenez', email = 'gjimenez@correo.co' )
    # inserted_records = PersonDao .insert( person_1 )
    # log .debug( f'Personas insertadas: { inserted_records }' )

    # ? Actualizar un registro
    # person_1 = Person( 3, 'Germán Darío', 'Jiménez Gutiérrez', 'gjimenez@correo.co' )
    # updated_records = PersonDao .update( person_1 )
    # log .debug( f'Personas actualizadas: { updated_records }' )

    # ? Eliminar un registro
    # person_1 = Person( id = 3 )
    # deleted_records = PersonDao .delete( person_1 )
    # log .debug( f'Personas eliminadas: { deleted_records }' )

    # ? Mostrar todos los registros
    people = PersonDao .select()
    for person in people :
        log .debug( person )