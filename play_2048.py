# Script que ejecuta el juego 2048

# importamos el resto de módulos propios

import display

import tablero

import players

import guardado

import time

from os import system

from os.path import exists

from random import randint

import sqlite3


# Creamos la clase para el motor del juego, y después lo arrancamos.

class Motor(object):


    def arrancar_partida(self, player, display):

        continuar = True

        while continuar:
            eleccion = display.interactivo_pral_usuario(player)

            if eleccion == "n" or eleccion == "N":
                self.jugar_partida(player, display)
                player.tablero = tablero.Tablero() #Reiniciamos el tablero del jugador

            elif eleccion == "c" or eleccion == "C":
                print("Elige la partida para cargar:\n")
                guardado.mostrar_partidas_DB(player)
                para_cargar = input("> ")
                guardado.cargar_tablero_a_jugador(player, para_cargar) # Falta por implementar el sistema de guardado.
                self.jugar_partida(player, display)
                player.tablero = tablero.Tablero()

            elif eleccion == "r" or eleccion == "R":
                guardado.mostrar_ranking_jugadores() # Falta implementar el ranking (será leer un fichero)

            elif eleccion == "s" or eleccion == "S":
                print(f"Hasta pronto {player.nombre}.\nRETURN...")
                input()
                continuar = False

            elif eleccion == "d" or eleccion =="D":
                system("clear")
                print("Introduce la contraseña para ELIMINAR las partidas: ")
                contraseña = input("> ")

                if contraseña == "4dri4N":
                    system("rm 2048DB.db")
                    print("La database con las partidas ha sido ELIMINADA.")
                    print("Se procede a reiniciar el juego...")
                    input()

                    system("python play_2048.py")
                    exit()

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
                    print("Desea guardar partida? ")
                    respuesta = input("> ")

                    if respuesta in "sisíSiSí":
                        print("¿Con qué nombre: ?")
                        nombre_partida_para_guardar = input("> ")
                        guardado.guardar_tableroDB(player, nombre_partida_para_guardar)

                    else:
                        pass
                    continuar = False

                    # Actualizamos si es necesario la puntuacion máxima.
                    if player.puntuacion > player.puntuacion_maxima:
                        player.puntuacion_maxima = player.puntuacion

                    player.puntuacion = 0

                else:
                    pass

            else:
                continuar = False


#######################
###  Tests ############
#######################

if exists("2048DB.db"):
    pass

else:
    guardado.crear_DB_sistema_guardado()

player = players.Player()

player.tablero = tablero.Tablero()

display = display.Pantalla()

display.interactivo_intro_player(player)

motor = Motor()

motor.arrancar_partida(player, display)
