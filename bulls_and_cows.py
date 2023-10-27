"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Bulls & Cows ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""
import random
import time
import datetime

def time_format(start, stop):
    """Time formatting function"""
    el_time = int(round((stop - start), 0))
    el_time_min = el_time // 60
    el_time_sec = el_time % 60
    el_time = f"Elapsed time: {el_time_min}min {el_time_sec}sec"
    return el_time

def num_gen():
    """Generates a random number and a list with indexes for each digit"""
    a = str(random.randint(1000, 9999))
    a_list = list(enumerate(a))
    print(a) #just for checking
    return a, a_list

def bull_cow(a_number, b_number):
    """Generates a list with indexes for each digit
    Conditions whether it\'s bull or cow
    Showing how many b/c"""
    b_list = list(enumerate(b_number))
    cows = []
    bulls = []
    for index, cislo in b_list:
        if cislo ==  a_list[index][1]:
            bulls.append(cislo)
        else:
            if cislo in a_number and cislo not in cows:
                cows.append(cislo)
    print(f"{len(bulls)} bulls, {len(cows)} cows")
    print(sline) 
    return bulls

def final_result(bulls: int) -> str:
    """Shows the final result - number of guesses"""    
    if len(bulls) == 4:
        print(f"Correct, you've guessed the right number in {guesses} guess!") if guesses == 1 else print(f"Correct, you've guessed the right number in {guesses} guesses!")
        if guesses < 4:
            print("That`s amazing")
        elif guesses < 7:
            print("Average score")
        else:
            print("Not so good...")
        return False
    else:
        return True
    
def game_round(input):
    """Game round.
    -> Counts numer of guesses
    -> Checks the input (only digits, 4 digits,  from 1000 - 9999)
    """
    guesses = 0
    game_round = True
    while game_round:
        if not input.isnumeric():
            print("You must type only digits")
        elif len(input) != 4:
            print("The number must be 4 digits long")
        elif input[0] == "0":
            print("The number must be between 1000-9999")
        else:
            #---Counting guesses
            guesses = guesses + 1
            #---Conditions whether it's bull or cow
            bulls = bull_cow(a_number, input)
            #---Showing the final result
            game_round = final_result(bulls)
                
def play_again() -> bool:
    """Play again - function"""
    cont_game = True
    while cont_game: 
        x = input("Do you want to play again? (y/n): ")
        if x == "y":
            cont_game = False
            return True
        elif x == "n":
            cont_game = False
            return False
        else:
            print("Must type - 'y'/'n'")

def score():
    """Writing score to score.txt file"""
    date = datetime.datetime.now()
    fdate = date.strftime("%x")
    txt_file = open("score.txt", mode="a")
    txt_file.write(f"\nDate: {fdate} | {user: <10}| Guesses: {guesses: <3}| {time_format(start_time, end_time)}")
    txt_file.close()



            
#---Auxiliary variables
sline = "-" * 50
game_on = True

#---Main game loop
print("\nHi there!")
while game_on:
    user = input(f"{sline}\nWhat's your name? ")
    if len(user) <= 0:
        print("You're name must be at least 1 character long!")
    else:
        #---Time stamp - start
        start_time = time.time()
        print(f"{sline}\nI`ve generated a random 4 digit number for you. \nLet's play a bulls and cows game.\n{sline}")
        #---Random number
        a_number, a_list = num_gen()
        guesses = 0
        #---Game round
        game_round(input("Enter a number: "))
        #---Time stamp - end
        end_time = time.time()
        #---Elapsed time
        print(time_format(start_time, end_time))
        #---Writing score to a .txt
        score()
    #---Play again
    game_on = play_again()
        
print(f"{sline}\nThank you for your game\nBye!")    


