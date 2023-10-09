"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Tic-tac-toe ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""

board = ["","","","","","","","",""]
def grid():
    return print(f"""
        +---+---+---+
        |{board[0] :^3}|{board[1] :^3}|{board[2] :^3}|
        +---+---+---+
        |{board[3] :^3}|{board[4] :^3}|{board[5] :^3}|   
        +---+---+---+         
        |{board[6] :^3}|{board[7] :^3}|{board[8] :^3}| 
        +---+---+---+  
          """)
def winner():
    #condition checking whether one of player won
        for i in range(0, 9, 3):
            if board[i:i+3] == ["o", "o", "o"]:
                print("Player o won!")
            elif board[i:i+3] == ["x", "x", "x"]:
                print("Player x won!")
        for i in range(0, 3):
            if board[i:i+7:3] == ["o", "o", "o"]:
                print("Player o won! |")
            elif board[i:i+7:3] == ["x", "x", "x"]:
                print("Player x won! |")
        if board[::4] == ["o", "o", "o"]:
            print("Player o won! \\")
        elif board[::4] == ["x", "x", "x"]:
            print("Player x won! \\")
        if board[2:7:2] == ["o", "o", "o"]:
            print("Player o won! /")
        if board[2:7:2] == ["x", "x", "x"]:
            print("Player x won! /")

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

game_on = True
while game_on:
    print("Let\'s start the game\n" + "-" * 40)
    round = 1
    while round < 9:
        grid()
        print(f"{round}. round\n{'-' * 40}")
        round += 1
        
        pl_o = True
        while pl_o:
            #player o input
            player_o = int(input("Player o | Your move number: "))
            #range condition
            if player_o == 0 or player_o > 9:
               print("You can place your stone only between numbers 1 to 9!")
            else:
                player_o -= 1
                if board[player_o] != "":
                    print("\n","!" * 30, "\nYou can`t put your stone here\n!!!")
                else:
                    board[player_o] = "o"   # umístění kamenu
                    pl_o = False
        grid()
        if winner():
            winner()
            round = False
        else:
            pl_x = True
            while pl_x:
                #player x input
                player_x = int(input("Player x | Your move number: "))
                #range condition
                if player_x == 0 or player_x > 9:
                    print("You can place your mark only between numbers 1 to 9!")
                else:
                    player_x -= 1
                    if board[player_x] != "":
                        print("\n","!" * 30, "\nYou can`t put your mark here\n!!!")
                    else:
                        board[player_x] = "x"   # umístění kamenu
                        if winner():
                            grid()
                            winner()
                        else:
                            pl_x = False
    print("What the fuck")                