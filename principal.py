#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from extras import *
from funciones import *


#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()
        #pygame.mixer.music.load("")#cargamos la musica para el juego

        #pygame.mixer.music.play()#le damos play a la musica

        #Preparar la ventana
        pygame.display.set_caption("Armando Palabras")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = 0;

        puntos = 0
        palabra = ""
        letras = []
        posiciones = []
        lemario=[]

        archivo= open("lemario.txt","r")
        for linea in archivo.readlines():
            lemario.append(linea[0:-1])

        dibujar(screen, palabra, letras, posiciones, puntos, 61 - segundos )


        while segundos < 61:

            #dejar pasar tiempo para ir a 40 fps
            gameClock.tick(40)
            totaltime += gameClock.get_time()

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabra += letra
                    if e.key == K_BACKSPACE:
                        palabra = palabra[0:len(palabra)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(palabra, letras, posiciones, lemario)
                        palabra = ""

            segundos = pygame.time.get_ticks()/1000;

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, palabra, letras, posiciones, puntos, 61 - segundos )

            pygame.display.flip()

            actualizar(letras, posiciones)

        while 1:
            #tiempo total
            gameClock.tick(40)
            totaltime += gameClock.get_time()

            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
            #pygame.mixer.music.stop()
#Programa Pirncipal ejecuta Main
if __name__ == "__main__":
    main()
