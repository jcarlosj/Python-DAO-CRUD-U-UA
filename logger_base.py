import logging as log

# ! Logging: Rastrea eventos que suceden cuando se ejecuta una aplicación
log .basicConfig( level = log .DEBUG )      #   Si no se establece esta configuración se desplegarán los mensajes del nivel de Warning en adelante 


if __name__ == '__main__' :
    # ! Mostramos mensajes en cada uno de los niveles de gravedad permitidos
    # Ref: https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

    log .debug( 'Mensaje a nivel DEBUG' )               #   Nivel 0 de Depuracción
    log .info( 'Mensaje a nivel INFO' )                 #   Nivel 1 de Confirmación
    log .warning( 'Mensaje a nivel WARNING' )           #   Nivel 2 de Advertencia (predeterminado)
    log .error( 'Mensaje a nivel ERROR' )               #   Nivel 3 de Error
    log .critical( 'Mensaje a nivel CRITICAL' )         #   Nivel 4 de Critico
