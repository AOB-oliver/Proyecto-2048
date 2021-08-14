# En este script queremos desarrollar clases y methods para los jugadores.
#
# Sus datos como jugador y los methods para guardar partida.
import time

from os import system

from random import randint

from os.path import exists

###############
# C L A S E S #
###############

class Player(object):

    nombre = None
    puntuacion = None
    tablero = None
    partidas_guardadas = []

    def intro_player(self):
        print("Introduce nombre de jugador: ")
        self.nombre = input("> ")
        print(f"Has introducido: {self.nombre}. ¿Estás de acuerdo?")
        correcto = input("> ") in "sisíSiSí"

        if correcto:
            print("Tu nombre ha sido guardado.")

        else:
            pass
        # Como se utilizará desde un método de mostrar en pantalla, devuelve
        # correcto para saber cuando dejar de pedir, nombre de usuario
        return correcto

    # Hay que revisar este method.
    # Pro: El código funciona.
    # Con: Hay que pensar como queremos hacer funcionar el sistema de guardado.
    # Extra: En el módulo [[ os ]] hay funciones que pueden gestionar archivos
    #       sin necesidad de escribir directamente a traves de [[ system() ]].
    def crear_dir_player(self):
        print(f"Se va a crear el directorio player_{self.nombre}. ¿Estás de acuerdo?")
        correcto = input("> ") in "sisíSiSí"

        if correcto:
            system(f"mkdir player_{self.nombre}")
            nombre_archivo = "player_" + self.nombre
            print(f"Directorio creado: {exists(nombre_archivo)}")
            system("ls -R")
            input()
            system("clear")

        else:
            print("No se ha creado el directorio. ¿Quiere volver a intentarlo?")
            correcto = input("> ") in "sisíSiSí"

            if correcto:
                self.crear_dir_player()
            else:
                pass
