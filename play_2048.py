# Script que ejecuta el juego 2048

# importamos el resto de módulos propios

import display

import tablero

import players

import time

from os import system

from random import randint


# Creamos la clase para el motor del juego, y después lo arrancamos.

class Motor(object):


    def arrancar_partida(self, player, display):

        continuar = True

        while continuar:
            eleccion = display.interactivo_pral_usuario(player)

            if eleccion == "n" or eleccion == "N":
                self.jugar_partida(player, display)

            elif eleccion == "c" or eleccion == "C":
                pass # Falta por implementar el sistema de guardado.

            elif eleccion == "r" or eleccion == "R":
                pass # Falta implementar el ranking (será leer un fichero)

            elif eleccion == "s" or eleccion == "S":
                print(f"Hasta pronto {player.nombre}.\nRETURN...")
                input()
                continuar = False

            else:
                pass # Por como funciona displa.interactivo_pral_usuario, esto
                     # esto no puede ocurrir.

    def jugar_partida(self, player, display):
        continuar = True

        while continuar:

            player.tablero.introduce_aleatorio()

            if player.tablero.comprobar_continuidad():

                eleccion = display.interactivo_tablero_partida(player)

                if eleccion == "arriba":
                    player.tablero.desplazar_arriba()

                elif eleccion == "izquierda":
                    player.tablero.desplazar_izquierda()

                elif eleccion == "abajo":
                    player.tablero.desplazar_abajo()

                elif eleccion == "derecha":
                    player.tablero.desplazar_derecha()

                elif eleccion == "salir":
                    continuar = False

                else:
                    pass

            else:
                continuar = False


#######################
###  Tests ############
#######################

player = players.Player()

player.nombre = player.intro_player()

player.tablero = tablero.Tablero()

display = display.Pantalla()

motor = Motor()

motor.arrancar_partida(player, display)
