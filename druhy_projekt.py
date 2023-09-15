"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Bulls & Cows ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""

#TODO naimportuj potřebné knnihovny a moduly
import random

#pomocné proměnné
sline = "-" * 50
game_on = True

#opakující se smyčka - hra
print("Hi there!\n" + sline)
while game_on:
    #TODO pozdrav
    print("I`ve generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print(sline)
    a_number = str(random.randint(1000, 9999))
    print(a_number)
    #TODO while smyčka hádání čísla
    while True:
        b_number = input("Enter a number: ")
        #podminky, hlidani aby byly cisla 4, nezacinala 0 a byly všechny numerické
        if not b_number.isnumeric():
            print("You must type only digits")
        elif len(b_number) != 4:
            print("The number must be 4 digits long")
        elif b_number[0] == "0":
            print("The first digit must be between 1 - 9")
        else:
            print(b_number)
            a_list = list(enumerate(a_number)) #vytvoření indexů pro čísla
            b_list = list(enumerate(b_number))
            print(a_list)
            print(b_list)

            cows = []
            bulls = []
            #budeme porovnávat 1. jestli jsou zadaná čísla na indexech -> bulls
            #a jestli se nacházi v čísle -> cows
            for index, cislo in b_list:
                if cislo ==  a_list[index][1]:
                    print("Bull")
                    bulls.append(cislo)
                else:
                    if cislo in a_number and cislo not in cows:
                        print("cow")
                        cows.append(cislo)
            
            break
    break
print(bulls)
print(cows)

            #for b in b_number:
            #    if b in a_number and b not in cows:
            #        
            #        print("je tam, ale na na mistě - cows")
            #        # vytvoř list kde uchováš cows
            #        cows.append(b)
            #        print(cows) 
            #    #else:

                
            #    for j in int(b_number):
            #        if j == i:

            #TODO smyčka for bude iterovat hadane cislo a porovnavat s inputem uzivatele
           # print("OK")
        
   

#TODO Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky

# TODO program vyhodnoti tip uzivatele - bull cisla na spravnem miste, cow - uhadnuta cisla ale na jiných pozicích

# TODO počítej čas jaký uplyne než hráč uhodne výsledek

# TODO zapiš do textového souboru prubeh hry - počet odhadu a cas
