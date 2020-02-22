import pygame
from pygame.locals import *
from configuracion import *
import winsound
import random

def nuevaLetra():
    vocales = ['a', 'e','i','o','u']
    normales = ['b','c','d','f','g','h','i','l','m','n','p','q','r','s','t','u','v']
    dificiles = ['j', 'k','w','x','y','z']
    n = random.random()
    if n < 0.35:
        return (random.choice(vocales))
    elif(n<0.95):
        return (random.choice(normales))
    else:
        return (random.choice(dificiles))

def actualizar(letras, posiciones):
    ## eliminar viejas
    for i in range(len(letras)-1,-1,-1):
        if(posiciones[i].y < 520):
            posiciones[i] = Punto(posiciones[i].x, (posiciones[i].y+1)) ## Esta line aquedo complicada porque son inmutables las tuplas
        else:
            letras.pop(i)
            posiciones.pop(i)

    ## agregar nuevas
    if(random.random()< 0.04):
        letras.append(nuevaLetra())
        posiciones.append(Punto(random.randint(10,ANCHO-10), -10))


def dameLetraApretada(key):
    winsound.PlaySound("boton.wav",winsound.SND_ASYNC)
    if key == K_a:

        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)

def cargar_imagen(filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


def dibujar(screen, candidata, letras, posiciones, puntos, segundos):

    imagen = cargar_imagen("fondo1.png",False)
    screen.blit(imagen, (0, 0))

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)


    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    for i in range(len(letras)):
        screen.blit(defaultFont.render(letras[i], 1, COLOR_LETRAS), posiciones[i])

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))