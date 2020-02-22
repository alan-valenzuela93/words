from principal import *
from configuracion import *
import math

# Esta funcion calcula los puntos de una palabra, ya esta probada y no debe modificarse
def puntos(candidata):
    return(int(math.pow(1.7,len(candidata))))



def cantApariciones (caracter,cadena): # Al darle un caracter y una cadena: cuenta cuantas veces encuentra
                                       # ese caracter en esa cadena y devuelve la cantidad de apariciones.
    aparece=0
    for letra in cadena:
        if letra==caracter:
            aparece+=1
    return aparece


def esta(letra,palabra):  #Al darle una letra y una palabra: devuelve True si esa letra
                          #aparece en la palabra. De cualquier otra forma, devuelve False.
    pertenece=False
    for caracter in palabra:
        if letra==caracter:
            pertenece=True
    return pertenece


def esValida(palabra,sopaLetras):

    nuevaCadena=""
    for letra in palabra:
        if cantApariciones(letra,sopaLetras)>=cantApariciones(letra,palabra): #Compara la cantidad de apariciones de una misma letra en la palabra y en la sopaLetras.
            if not esta(letra,nuevaCadena): #Si la letra no esta en mi nueva cadena, entonces la agrega, si ya esta no hace nada.
                nuevaCadena=nuevaCadena+letra*cantApariciones(letra,palabra) #En mi nueva cadena guarda las letras encontradas y la cantidad de veces que esten repetidas.
        else: #Si la cantidad de letras que estan en mi sopaLetras no son las necesarias para armar mi palabra retorna False
            return False
    return True

def quitar(letra, listaLetras, posiciones):

        if letra in listaLetras: #Solo funciona si esta la letra en la lista de letras, sino no hace nada
            posicionPrimeraVez=listaLetras.index(letra) #busca la posicion en la que aparece por primera vez la letra
            listaLetras.pop(posicionPrimeraVez) #elimina esa letra
            posiciones.pop(posicionPrimeraVez) #elimina esa posicion en la que aparece la letra

def procesar(palabra, letras, posiciones, lemario):

    puntaje = 0
    if not esValida(palabra,letras) or not esta(palabra,lemario): #la letra/palabra solo sera valida si puede formarse con las letras de la pantalla y que sea una palabra del lemario
        return puntaje #retorna 0 puntos
    else:
        for caracter in palabra: #si es valida la recorre y las quita de la pantalla y suma puntos
            quitar(caracter,letras,posiciones)
        puntaje = puntos(palabra)
    return puntaje #retorna los puntos que sume el usuario (si es valido, sino devuelve 0)
