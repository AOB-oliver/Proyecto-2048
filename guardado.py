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
    nombre_partida TEXT,
    puntuacion INTEGER,
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
    mat16 INTEGER
    );
    """)

    # Guardamos cambios y "cerramos conexión".
    conn.commit()
    conn.close()

# Ahora queremos que nos muestre los jugadores que tiene la DB:
def mostrar_jugadores_en_DB():
    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()

    for fila in c.execute('SELECT nombre FROM jugadores'):
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
    c.execute('SELECT nombre FROM jugadores')

    # Nos aseguramos de que el nombre exista en la DB:
    if (nombre,) in c.fetchall():
        c.execute('SELECT id FROM jugadores WHERE nombre = ?', (nombre,))
        player.id_DB = c.fetchone()[0]
        c.execute('SELECT nombre FROM jugadores WHERE nombre = ?', (nombre,))
        player.nombre = c.fetchone()[0]
        c.execute('SELECT puntuacion_max FROM jugadores WHERE nombre = ?', (nombre,))
        player.puntuacion_maxima = c.fetchone()[0]
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
            cargado = False

        else:
            cargado = False

    return cargado

# Implementamos ahora el ranking. Mediante sql es sencillo:
def mostrar_ranking_jugadores():

    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()

    for fila in c.execute('SELECT nombre, puntuacion_max FROM jugadores ORDER BY puntuacion_max;'):
        print(f"\n{fila[1]} ···· {fila[0]}")

    input() # Una pausa para que no nos lo salte.

    conn.commit()
    conn.close()

# Implementamos la introducción del tablero de un jugador.
def guardar_tableroDB(player, nombre_para_guardar):
    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()

    para_introducir = (
        player.id_DB,
        nombre_para_guardar,
        player.puntuacion,
        player.tablero.disposicion[0][0],
        player.tablero.disposicion[0][1],
        player.tablero.disposicion[0][2],
        player.tablero.disposicion[0][3],
        player.tablero.disposicion[1][0],
        player.tablero.disposicion[1][1],
        player.tablero.disposicion[1][2],
        player.tablero.disposicion[1][3],
        player.tablero.disposicion[2][0],
        player.tablero.disposicion[2][1],
        player.tablero.disposicion[2][2],
        player.tablero.disposicion[2][3],
        player.tablero.disposicion[3][0],
        player.tablero.disposicion[3][1],
        player.tablero.disposicion[3][2],
        player.tablero.disposicion[3][3],
        )

    c.execute("""
    INSERT INTO partidas (
    id,
    id_del_jugador,
    nombre_partida,
    puntuacion,
    mat1,
    mat2,
    mat3,
    mat4,
    mat5,
    mat6,
    mat7,
    mat8,
    mat9,
    mat10,
    mat11,
    mat12,
    mat13,
    mat14,
    mat15,
    mat16
    )
    VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, para_introducir)


    print("\nSe ha guardado correctamente.\n\nRETURN para continuar...")
    input()


    conn.commit()
    conn.close()

# Definimos ahora una funcion para guardar un jugador en la DB.
# return True o False dependiendo de si ha podido o no guardarlo.
def guardar_jugador_nuevo_DB(player):
    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()

    # Comprobamos si el nombre no está ya en uso en la DB:
    c.execute('SELECT nombre FROM jugadores')
    nombres = c.fetchall()
    input()

    if nombres == None:
        nombres = []

    else:
        pass

    disponible = (player.nombre,) not in nombres

    if disponible:

        para_introducir = (player.nombre, 0)
        c.execute('INSERT INTO jugadores (id, nombre, puntuacion_max) VALUES (NULL, ?, ?)', para_introducir)
        c.execute('SELECT id FROM jugadores WHERE nombre=?', [player.nombre])
        player.id_DB = c.fetchone()[0]
        bandera = True


    else:
        print("El nombre no está disponible... RETURN para continuar.")
        input()
        bandera = False


    conn.commit()
    conn.close()

    return bandera

# Funcion para cargarle un tablero a un jugador:
def cargar_tablero_a_jugador(player, nombre_partida_guardada):

    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()
    c.execute('SELECT nombre_partida FROM partidas')
    partidas = c.fetchall()
    # Nos aseguramos de que el nombre exista en la DB:
    if (nombre_partida_guardada,) in partidas:
        c.execute('SELECT mat1 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[0][0] = c.fetchone()[0]
        c.execute('SELECT mat2 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[0][1] = c.fetchone()[0]
        c.execute('SELECT mat3 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[0][2] = c.fetchone()[0]
        c.execute('SELECT mat4 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[0][3] = c.fetchone()[0]

        c.execute('SELECT mat5 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[1][0] = c.fetchone()[0]
        c.execute('SELECT mat6 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[1][1] = c.fetchone()[0]
        c.execute('SELECT mat7 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[1][2] = c.fetchone()[0]
        c.execute('SELECT mat8 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[1][3] = c.fetchone()[0]

        c.execute('SELECT mat9 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[2][0] = c.fetchone()[0]
        c.execute('SELECT mat10 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[2][1] = c.fetchone()[0]
        c.execute('SELECT mat11 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[2][2] = c.fetchone()[0]
        c.execute('SELECT mat12 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[2][3] = c.fetchone()[0]

        c.execute('SELECT mat13 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[3][0] = c.fetchone()[0]
        c.execute('SELECT mat14 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[3][1] = c.fetchone()[0]
        c.execute('SELECT mat15 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[3][2] = c.fetchone()[0]
        c.execute('SELECT mat16 FROM partidas WHERE nombre_partida = ?', [nombre_partida_guardada])
        player.tablero.disposicion[3][3] = c.fetchone()[0]


        cargado = True
        conn.commit()
        conn.close()

    else:
        print("No se encuentra esa partida en la memory-card... RETURN para continuar.")
        input()
        cargado = False
        conn.commit()
        conn.close()



    return cargado

# Implementamos que muestren las partidas del usuario
def mostrar_partidas_DB(player):
    conn = sqlite3.connect('2048DB.db')
    c = conn.cursor()
    c.execute('SELECT id FROM jugadores WHERE nombre = ?', (player.nombre,))
    key = int(c.fetchone()[0])

    for fila in c.execute('SELECT nombre_partida FROM partidas WHERE id_del_jugador = ?', (key,)):
        print(fila)

    conn.close()
