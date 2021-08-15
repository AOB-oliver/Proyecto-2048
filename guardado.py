# Implementamos aquí las funciones para guardar a los jugadores y sus partidas.

# Vamos a crear dos tablas. Una con jugadores guardados, y otra para guardar
# partidas.

#
# jugadores ( id, nombre, puntuacion_maxima)
# partidas (id, id_del_jugador, puntuacion, mat1, mat2, ... , mat16)
#

# Modulos necesarios

import sqlite3 # API para trabajar con SQL

from os.path import exists # Querremos saber si la base de datos ya esta creada

from textwrap import dedent



# La primera función es para crear la estructura de la DB en caso de que el
# juego se ejecute desde un nuevo directorio o equipo.
def crear_DB_sistema_guardado():

    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()

    # Tabla para los jugadores
    c.execute("""CREATE TABLE jugadores (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    puntuacion_max INTEGER
    );
    """
    )

    # Tabla para las partidas
    c.execute("""CREATE TABLE partidas (
    id INTEGER PRIMARY KEY,
    id_del_jugador INTEGER,
    puntuacion INTEGER,
    mat INTEGER,
    mat1 INTEGER,
    mat2 INTEGER,
    mat3 INTEGER,
    mat4 INTEGER,
    mat5 INTEGER,
    mat6 INTEGER,
    mat7 INTEGER,
    mat8 INTEGER,
    mat9 INTEGER,
    mat10 INTEGER,
    mat11 INTEGER,
    mat12 INTEGER,
    mat13 INTEGER,
    mat14 INTEGER,
    mat15 INTEGER,
    mat16 INTEGER,
    );
    """)

    # Guardamos cambios y "cerramos conexión".
    conn.commit()
    conn.close()

# Ahora queremos que nos muestre los jugadores que tiene la DB:
def mostrar_jugadores_en_DB():
    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()

    for fila in c.execute('SELECT nombre FROM jugadores;'):
        print(fila)

    conn.close()

# Esta funcion cargará en el objeto [[ player ]] introducido un jugador existente
# en la DB. Tendrá en cuenta la posibilidad de que el nombre introducido no
# esté en la DB.
#
# return cargado, para que en play_2048.py sepamos si se ha cargado o no el
# jugador.
def cargar_jugador_desde_DB(nombre, player):
    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()

    # Nos aseguramos de que el nombre exista en la DB:
    if nombre in c.execute('SELECT nombre FROM jugadores;'):
        player.nombre = c.execute('SELECT nombre FROM jugadores;')[1]
        player.puntuacion_maxima = c.execute('SELECT nombre FROM jugadores;')[2]
        cargado = True
        conn.commit()
        conn.close()

    else:
        print("El nombre introducido no está en la base de datos...")
        print(dedent("""
        --> Introducir de nuevo (s)

        --> Salir (RETURN)

        """))
        eleccion = input("> ")

        if eleccion in "sS":
            cargar_jugador_desde_DB(nombre, player)

        else:
            cargado = False

    return cargado
