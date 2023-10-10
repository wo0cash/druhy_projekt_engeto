"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Tic-tac-toe ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""
import os

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
def check_winner():
#condition checking whether one of the players won
    for i in range(0, 9, 3):
        if board[i:i+3] == ["o", "o", "o"]:
            return "o!"
        elif board[i:i+3] == ["x", "x", "x"]:
            return "x"
    for i in range(0, 3):
        if board[i:i+7:3] == ["o", "o", "o"]:
            return "o"
        elif board[i:i+7:3] == ["x", "x", "x"]:
            return "x"
    if board[::4] == ["o", "o", "o"]:
        return "o"
    elif board[::4] == ["x", "x", "x"]:
        return "x"
    if board[2:7:2] == ["o", "o", "o"]:
        return "o"
    if board[2:7:2] == ["x", "x", "x"]:
        return "x"

def clear_scrn():
    if(os.name == 'posix'):
        return os.system('clear')
    else:
        return os.system('cls')

board = [""] * 9

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
* diagonal row""")

game_on = True
while game_on:
    print("=" * 40,"\nLet\'s start the game\n" + "-" * 40, "\n")
    round = 1
    while round <= 9:
        grid()
        print(f"{round}. round\n{'-' * 40}")
        
        if round % 2 == 1:
            player = "o"
        else:
            player = "x"
        while player:
            #player o input
            move = int(input(f"Player {player} | Your move number: "))
            #range condition
            if move == 0 or move > 9:
               print("You can place your stone only between numbers 1 to 9!")
            else:
                move -= 1
                if board[move] != "":
                    print("\n","!" * 30, "\nYou can`t put your stone here\n!!!")
                else:
                    board[move] = player   # umístění kamenu
                    break
         
        winner = check_winner()
        if winner:
            clear_scrn()
            grid()
            print(f"\n{'~' * 40}\nPlayer {winner} is a winner!!!\n{'~' * 40}\n")
            break
        elif round == 9:
            clear_scrn()
            grid()
            print("It's a tie!")    
            break
        round += 1

        clear_scrn()

    game = input("Do you wanna play again? (y/n)")        
    while game:
        if game == "n":
            game_on = False
            break
        elif game == "y":
            board = [""] * 9
            clear_scrn()
            break
        else:
            game = input(f'Must type "y" or "n"')
clear_scrn()
print("Thank you, goodbye!")


           