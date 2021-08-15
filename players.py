# En este script queremos desarrollar clases y methods para los jugadores.
#
# Sus datos como jugador y los methods para guardar partida.
import time

from os import system

from random import randint

from os.path import exists

import guardado

###############
# C L A S E S #
###############

class Player(object):

    nombre = None
    puntuacion = None
    puntuacion_maxima = None
    tablero = None
    id_DB = None

    def intro_player(self):
        print("Introduce nombre de jugador: ")
        self.nombre = input("> ")
        print(f"Has introducido: {self.nombre}. ¿Estás de acuerdo?")
        correcto = input("> ") in "sisíSiSí"

        if correcto:
            bandera = guardado.guardar_jugador_nuevo_DB(self)

            if bandera:
                 print("Tu nombre ha sido guardado.")

            else:
                pass
        else:
            pass
        # Como se utilizará desde un método de mostrar en pantalla, devuelve
        # correcto para saber cuando dejar de pedir, nombre de usuario
        return bandera
