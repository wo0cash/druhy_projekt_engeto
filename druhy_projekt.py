"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Bulls & Cows
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""

#TODO naimportuj potřebné knnihovny a moduly
import random
import os

#pomocné proměnné
sline = "-" * 50
game_on = True

#opakující se smyčka - hra
while game_on:
    #TODO pozdrav
    print("Hi there!\n" + sline + "\nI`ve generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print(sline)
    break
#TODO vytvoř 4 mistne cislo random nesmí začínát 0

#TODO Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky

# TODO program vyhodnoti tip uzivatele - bull cisla na spravnem miste, cow - uhadnuta cisla ale na jiných pozicích

# TODO počítej čas jaký uplyne než hráč uhodne výsledek

# TODO zapiš do textového souboru prubeh hry - počet odhadu a cas
