# Aquí el módulo destinado a los menús y disposición en pantalla.

import time

from os import system

from textwrap import dedent

import guardado


###############
# C L A S E S #
###############

class Pantalla(object):

    def cabecera(self):
        print(dedent("""
    ####################################
    #### 2 0 4 8 - T H E    G A M E ####
    ####################################
    """))


    # Los métodos que empiezan por 'menu' únicamente printean por pantalla.
    # Los métodos con 'intaractivo' llaman a los menús, y recogen además la
    # selección o la acción a ejecutar.

    def menu_intro_player(self):
        print(dedent("""

        T I E N E   Y A   U S U A R I O (?)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        |                                   |
        |       N U E V O  ··  press n/N    |
        |                                   |
        |                                   |
        |       B U S C A R ·· press b/B    |
        |                                   |
        |                                   |
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


        """))

    def interactivo_intro_player(self, player):
        system("clear")
        self.cabecera()
        self.menu_intro_player()

        eleccion = input("> ")

        if eleccion in "nN":
            # Esta bandera está explicada en players.py en el método intro_player()
            correcto = player.intro_player()

            if correcto:
                pass

            else:
                self.interactivo_intro_player(player)

        elif eleccion in "bB":
            guardado.mostrar_jugadores_en_DB()
            print("\n¿Qué usuario quieres cargar?\n")
            nombre = input("> ")
            cargado = guardado.cargar_jugador_desde_DB(nombre, player)

            if cargado:
                pass

            else:
                self.interactivo_intro_player(player)
        else:
            self.interactivo_intro_player(player)


    def menu_pral_usuario(self, player):
        print(dedent(f"""

        Q U E   H A C E R {player.nombre} (?)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        |                                   |
        |      Nueva partida ·· press n/N   |
        |                                   |
        |     Cargar partida ·· press c/C   |
        |                                   |
        |            Ranking ·· press r/R   |
        |                                   |
        |              Salir ·· press s/S   |
        |                                   |
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        """))

    def interactivo_pral_usuario(self, player):
        system("clear")
        self.cabecera()
        self.menu_pral_usuario(player)
        eleccion = input("> ")

        if eleccion in "nNcCrRsS":
            return eleccion

        else:
            return self.interactivo_pral_usuario(player)


    # Este menú será con el que realmente juguemos la partida. Mostrará la cabe-
    # cera, el tablero en cada momento, y las diferentes opciones
    def menu_tablero_partida(self, player):

        self.cabecera()
        print(f"Puntuación: {player.tablero.mayor_numero()}")
        player.puntuacion = player.tablero.mayor_numero()
        player.tablero.print_tablero()
        print(dedent("""

        I Z Q (a)  ·  A R R I B A (w)  ·  A B A J O (s)  ·  D E R (d)

                              S A L I R (:q)

        """))

    def interactivo_tablero_partida(self, player):

        system("clear")
        self.menu_tablero_partida(player)
        eleccion = input("> ")

        if eleccion in "aA":
            return "izquierda"

        elif eleccion in "wW":
            return "arriba"

        elif eleccion in "sS":
            return "abajo"

        elif eleccion in "dD":
            return "derecha"

        elif eleccion == ":q" or eleccion == ":Q":
            return "salir"

        else:
            print("\nEl comando no es válido... ")
            time.sleep(1)
            return self.interactivo_tablero_partida(player)
