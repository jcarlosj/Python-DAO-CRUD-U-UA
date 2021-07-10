from logger_base import log

# Definicion de la clase
class Person :

    def __init__( self, id = None, fname = None, lname = None, email = None ) :
        self ._id = id
        self ._first_name = fname
        self ._last_name = lname
        self ._email = email

    def __str__( self ) :
        return f'''
            { type( self ) .__name__ }
            id: { self ._id }
            first_name: { self ._first_name }
            last_name: { self ._last_name }
            email: { self ._email }
        '''

    # Getters & Setters
    @property
    def id( self ) :
        return self ._id

    @id .setter
    def id( self, id ) :
        self._id = id

    @property
    def first_name( self ) :
        return self ._first_name

    @first_name .setter
    def first_name( self, fname ) :
        self._first_name = fname

    @property
    def last_name( self ) :
        return self._last_name

    @last_name .setter
    def last_name( self, lname ) :
        self .last_name = lname

    @property
    def email( self ) :
        return self._email

    @email .setter
    def email( self, email ) :
        self._email = email

# ! Realizamos las respectivas pruebas a la clase
if __name__ == '__main__' :
    person_1 = Person( 1, 'Juan', 'Jimenez', 'jjimenez@correo.co' )
    log .debug( person_1 )      #   Debe estar activado en nivel debug para que este mensaje se visualice

    # ? Simulamos un insert, es decir no vamos a pasarle el id
    person_1 = Person( fname = 'Juan Carlos', lname = 'Jimenez Gutierrez', email = 'jcjimenezg@correo.co' )
    log .debug( person_1 )      #   Debe estar activado en nivel debug para que este mensaje se visualice

    # ? Simulamos un delete, solo pasaremos en id
    person_1 = Person( id = 1 )
    log .debug( person_1 )      #   Debe estar activado en nivel debug para que este mensaje se visualice
