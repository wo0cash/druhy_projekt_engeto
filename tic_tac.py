"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Tic-tac-toe ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""
import random
print("""
Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================""")

print("Let\'s start the game\n" + "-" * 40)

#TODO hra smyčka dokud hra neskončí
game_on = True
while game_on:
    #TODO list v listu 3x3 do kterého se budou doplňovat x a o
    grid = ["","","","","","","","",""]
    print(f"""
+---+---+---+
|{grid[0] :^3}|{grid[1] :^3}|{grid[2] :^3}|
+---+---+---+
|{grid[3] :^3}|{grid[4] :^3}|{grid[5] :^3}|   
+---+---+---+         
|{grid[6] :^3}|{grid[7] :^3}|{grid[8] :^3}| 
+---+---+---+  
          """)
    
    player_o = input("Player o | Please enter your move number: ")


#TODO input uživatele 1
#TODO input uživatele 2

#TODO symčka ověřující jsou 3 kameny h/v/diag jinak pokračuje hra

#TODO výhra
    break