import logging as log

file_name = 'capa_datos.log'

# ! Logging: Rastrea eventos que suceden cuando se ejecuta una aplicación
log .basicConfig(
    level = log .DEBUG,                                                             #   Si no se establece esta configuración se desplegarán los mensajes del nivel de Warning en adelante 
    format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',    #   Formatea registro en el log de la aplicacion
    datefmt = '%Y-%m-%d %I:%M:%S %p',                                               #   Formatea la fecha: %Y (año), %m (mes), %d (día), %I(hora) o %H (hora militar), %M: (minutos), %S (segundos), %p (am/pm)
    handlers=[                                                                      #   handlers: objetos son responsables de enviar los mensajes de registro apropiados
        log .FileHandler( file_name ),                                              #   Clase FileHandler: envía la salida del registro a un archivo de disco
        log .StreamHandler()                                                        #   Clase StreamHandler: envia la salida del registro a la consola
    ]
)
#   Usando el parametro posicional agrega al mensaje del log: 
#       %(asctime)s     --> fecha y hora
#       %(levelname)s   --> nivel (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#       %(filename)s    --> nombre del archivo
#       %(lineno)s      --> linea donde ocurrio el evento
#       %(message)s     --> mensaje que hemos agregado

if __name__ == '__main__' :
    # ! Mostramos mensajes en cada uno de los niveles de gravedad permitidos
    # Ref: https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

    log .debug( 'Mensaje a nivel DEBUG' )               #   Nivel 0 de Depuracción
    log .info( 'Mensaje a nivel INFO' )                 #   Nivel 1 de Confirmación
    log .warning( 'Mensaje a nivel WARNING' )           #   Nivel 2 de Advertencia (predeterminado)
    log .error( 'Mensaje a nivel ERROR' )               #   Nivel 3 de Error
    log .critical( 'Mensaje a nivel CRITICAL' )         #   Nivel 4 de Critico
