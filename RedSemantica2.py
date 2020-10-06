# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 22:51:53 2020

@author: Martinez Garcia Isabel y Luna Ganzáles Rocio
"""
import json
Animales = False


with open("Baseanimales.json", "r") as read_file:
     data = json.load(read_file)
     Animales = data['animales']   

def esta(A,B,C,CONI):
    i = 0
    while i<len(CONI):
        if CONI[i][0] == A:
            if CONI[i][1] == B:
                if CONI[i][2] == C:
                    return True
        i = i + 1 
    return False
       

def vervoEs(A,B,C):
    return  esta(A,B,C,Animales)
def vervoVive(A,B,C):
    return  esta(A,B,C,Animales)
def vervoTiene(A,B,C):
    return  esta(A,B,C,Animales)


def main():
    print("Biemvenidos al Zoologico")
    print('Puedes consultar escribiendo vervoEs(<"Animal">,<"Es">,<"Clasificacion">)')
    print('Puedes consultar escribiendo vervoVive(<"Animal">,<"Vive">,<"Lugar">)')
    print('Puedes consultar escribiendo vervoTiene(<"Animal">,<"Tiene">,<"Caracteristica">)')
    print("Para salir preciona 'q' o escribe quit()")
    Terminar = False
    while not Terminar:
        Leer = input(">")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)
if __name__ == "__main__":
    main()
    


