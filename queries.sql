CREATE DATABASE py_test;

DROP TABLE IF EXISTS people;
TRUNCATE TABLE people;

CREATE TABLE people(
  	id serial,
	first_name varchar( 30 ),
  	last_name varchar( 30 ),
  	email varchar( 50 ),
    primary key( id )
)

INSERT INTO people( first_name, last_name, email ) VALUES ( 'Juan Carlos', 'Jiménez Gutiérrez', 'jjimenez@correo.co' );
INSERT INTO people( first_name, last_name, email ) VALUES ( 'Janeth Eva Sofía', 'Gutiérrez González', 'jgutierrez@correo.co' );

SELECT * FROM people ORDER BY id;







