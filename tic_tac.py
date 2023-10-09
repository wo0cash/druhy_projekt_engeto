"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Tic-tac-toe ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""

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



#TODO hra smyčka dokud hra neskončí

board = ["","","","","","","","",""]

game_on = True
while game_on:
    print("Let\'s start the game\n" + "-" * 40)
    round = True
    while round:
        grid = f"""
        +---+---+---+
        |{board[0] :^3}|{board[1] :^3}|{board[2] :^3}|
        +---+---+---+
        |{board[3] :^3}|{board[4] :^3}|{board[5] :^3}|   
        +---+---+---+         
        |{board[6] :^3}|{board[7] :^3}|{board[8] :^3}| 
        +---+---+---+  
          """
        print(grid)
        
        #condition checking whether one of player won
        for i in range(0, 9, 3):
            if board[i:i+3] == ["o", "o", "o"]:
                print("Player o won!")
                print(grid)
            elif board[i:i+3] == ["x", "x", "x"]:
                print("Player x won!")
                print(grid)
        for i in range(0, 3):
            if board[i:i+7:3] == ["o", "o", "o"]:
                print("Player o won! |")
                print(grid)
            elif board[i:i+7:3] == ["x", "x", "x"]:
                print("Player x won! |")
                print(grid)
        for i in range(0, 3, 2):
            if board[i:i+9: 4] == ["o", "o", "o"]:
                print("Player o won! opacna")
            elif board[i:7:2] == ["o", "o", "o"]:
                print("Player o won! /")
        #player`s input
        player_o = int(input("Player o | Please enter your move number: "))
        #range condition
        if player_o == 0 or player_o > 9:
            print("You can place your stone only between 1 to 9!")
        else:
            player_o -= 1
            #TODO symčka ověřující, že jsou 3 kameny h/v/diag jinak požádá o umístění jinde
            if board[player_o] != "":
                print("\n","!" * 30, "\nYou can`t put your stone here\n!!!")
            else:
                board[player_o] = "o"
                #TODO umístění kamenu
        
        
#TODO input uživatele 2



#TODO výhra
