# Queremos crear el juego de 2048 (2 ** 11)
#
# Este script se encarga de las funcionalidades relativas al tablero y sus
# movimientos.
#
# Imports necesarios
import time

from os import system

from random import randint

###############################################
### F U N C I O N E S - A U X I L I A R E S  ##
###############################################

# Necesitamos esta función para trabajar cómodamente con los movimientos del
# tablero.
def invertir_fila(fila):
    aux = []
    for i in range(0, len(fila)):
        aux.append(fila[len(fila)-1-i])

    return aux

# Para implementar los movimientos de panel, vamos a definir una función que
# rote una matriz en sentido antihorario.
def rotar_matriz(matriz):
    mat_aux = []

    # Aprovechamos que es cuadrada, para que el iterador sirva igualmente.
    for i in list(range(0, len(matriz))):
        fila_aux = []
        for j in list(range(0, len(matriz))):
            fila_aux.append(matriz[j][len(matriz)-1-i])
        mat_aux.append(fila_aux)

    return mat_aux

########################
#####  C L A S E S  ####
########################


# Queremos una [[clase]] que será la que corresponda a la "matriz" del juego.
class Tablero(object):
    """docstring for tablero. This is going to be a handmade matrix, with some
    methods for moving de matrix in the cardinal directions"""

    # Al crear un tablero, la disposición inicial es igual a 0.
    disposicion = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]

    # Queremos implementar la introducción de 1s o 2s de forma aleatoria en
    # el tablero.
    #
    # TENER EN CUENTA: se introduce de forma aleatoria y si el tablero fuera
    # mucho mayor, tendríamos problemas una vez queden pocos ceros ya que
    # en cuanto a eficiencia, tendría que iterar un número indeterminado de
    # veces para que diera con la localización "vacía"
    # ALTERNATIVA PARA REFINAR: primero conseguir el número de 0s que quedan
    # después, generar un entero aleatorio en el rango de 0s que hay.
    # con un contador, iterar la matriz contando 0s hasta dar con la posición
    # de cero que habíamos generado, y introducir ahí un aleatorio entre 1 y 2.
    def introduce_aleatorio(self):

        por_introducir = True


        while por_introducir:

            x = randint(0, 3)
            y = randint(0, 3)
            num_introducir = randint(1, 2)

            if self.disposicion[x][y] == 0:
                self.disposicion[x][y] = num_introducir
                por_introducir = False

            else:
                pass

    # Queremos comprobar si el tablero está lleno.
    #
    # Evitar así, que el [[while]] en [[introduce_aleatorio]] no tenga fin.
    def indicador_tablero_lleno(self):

        cuenta = 0
        for i in self.disposicion:
            cuenta += i.count(0)

        # IDEA -> Podría devolver también la propia cuenta por si en algún
        # momento queremos implementar que el player sepa cuantos huecos le
        # quedan.
        return cuenta == 0

    # Implementamos los methods destinados a mover el tablero
    #
    # Queremos que se desplacen los números, a menos que estén contra la
    # "pared", donde se quedarán quietos. Además, si un número se va a desplazar
    # sobre una casilla donde ha quedado el mismo número, estos se sumarán en
    # la casilla más cercana a la "pared" correspondiente a la dirección de
    # movimiento del method.
    #
    # Solo implementamos para derecha, y después implementaremos rotaciones
    # para utilizar el method para derecha y que mueva el tablero en el resto de
    # direcciones

    def desplazar_derecha(self):

        # Iteramos sobre las filas de derecha a izquierda:
        for i in self.disposicion:
            for j in invertir_fila(list(range(1,len(self.disposicion)))):

                if i[j] == 0:
                    i[j] = i[j-1]
                    i[j-1] = 0

                elif i[j] == i[j-1]:
                    i[j] = i[j] * 2
                    i[j-1] = 0

                else:
                    pass

    # El method para mover el panel a la izquierda vamos a implementalo utili-
    # zando el method desplazar a la derecha, haciendo una reflexión sobre la
    def desplazar_izquierda(self):

        matriz_auxiliar = Tablero()
        matriz_auxiliar.disposicion = self.disposicion

        # Rotamos, ejecutamos desplazamiento, y devolvemos al sitio.
        matriz_auxiliar.disposicion = rotar_matriz(rotar_matriz(matriz_auxiliar.disposicion))
        matriz_auxiliar.desplazar_derecha()
        matriz_auxiliar.disposicion = rotar_matriz(rotar_matriz(matriz_auxiliar.disposicion))

        self.disposicion = matriz_auxiliar.disposicion


    def desplazar_arriba(self):

        matriz_auxiliar = Tablero()
        matriz_auxiliar.disposicion = self.disposicion

        # Rotamos, ejecutamos desplazamiento, y devolvemos al sitio.
        matriz_auxiliar.disposicion = rotar_matriz(rotar_matriz(rotar_matriz(matriz_auxiliar.disposicion)))
        matriz_auxiliar.desplazar_derecha()
        self.disposicion = rotar_matriz(matriz_auxiliar.disposicion)

    def desplazar_abajo(self):

        matriz_auxiliar = Tablero()
        matriz_auxiliar.disposicion = self.disposicion

        # Rotamos, ejecutamos desplazamiento, y devolvemos al sitio.
        matriz_auxiliar.disposicion = rotar_matriz(matriz_auxiliar.disposicion)
        matriz_auxiliar.desplazar_derecha()
        self.disposicion = rotar_matriz(rotar_matriz(rotar_matriz(matriz_auxiliar.disposicion)))


    def mayor_numero(self):

        maxs = []
        for i in range(0, len(self.disposicion)):
            maxs.append(max(self.disposicion[i]))

        return max(maxs)


    # A tener en cuenta: con un for y la longitud del tablero, podemos parame-
    # trizar el print de forma que el method sea válido para cualquier tamaño.
    def print_tablero(self):
        x = self.disposicion
        print(f"""

        |{x[0][0]}\t|\t{x[0][1]}\t|\t{x[0][2]}\t|\t{x[0][3]}|

        |{x[1][0]}\t|\t{x[1][1]}\t|\t{x[1][2]}\t|\t{x[1][3]}|

        |{x[2][0]}\t|\t{x[2][1]}\t|\t{x[2][2]}\t|\t{x[2][3]}|

        |{x[3][0]}\t|\t{x[3][1]}\t|\t{x[3][2]}\t|\t{x[3][3]}|


        """)


    # Va a ser rudimentario. Tratemos de que sea lo menos aparatoso posible
    # Recorremos filas y columnas, buscando parejas adyacentes iguales, o 0s.
    def comprobar_continuidad(self):

        puede_continuar = False
        x = self.disposicion
        # Comprobamos por fila:
        for i in range(0, len(x)):
            for j in range(0, len(x[i])-1):

                if x[i][j] == 0 or x[i][j] == x[i][j+1] or x[i][j+1] == 0:
                    puede_continuar = True

        # Comprobamos por columnas
        for i in range(0, len(x)-1):
            for j in range(0, len(x[i])):

                if x[i][j] == 0 or x[i][j] == x[i+1][j] or x[i+1][j] == 0:
                    puede_continuar = True

        return puede_continuar


# TESTS
