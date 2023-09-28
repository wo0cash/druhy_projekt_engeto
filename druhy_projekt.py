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
#---Time formatting function
def time_format(start, stop):
    el_time = int(round((stop - start), 0))
    el_time_min = el_time // 60
    el_time_sec = el_time % 60
    el_time = f"Elapsed time: {el_time_min}min {el_time_sec}sec"
    return el_time


#---Auxiliary variables
sline = "-" * 50
game_on = True

#---Main game loop - Greeting, generating a 4 digit number and start time counting
print("Hi there!")
while game_on:
    guesses = 0
    start_time = time.time()
    print(sline + "\nI`ve generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print(sline)
    a_number = str(random.randint(1000, 9999))
    print(a_number) #just for checking
    #---Input form user -> guessing the number
    while True:
        b_number = input("Enter a number: ")
        #---Conditions, 4 digits, all digits, and [0] index != 0
        if not b_number.isnumeric():
            print("You must type only digits")
        elif len(b_number) != 4:
            print("The number must be 4 digits long")
        elif b_number[0] == "0":
            print("The first digit must be between 1 - 9")
        else:
            #---Counting guesses
            guesses = guesses + 1
            a_list = list(enumerate(a_number)) #generating indexes for each number
            b_list = list(enumerate(b_number))
        
            cows = []
            bulls = []
            #---Conditions whether it's bull or cow
            for index, cislo in b_list:
                if cislo ==  a_list[index][1]:
                    #print("Bull")
                    bulls.append(cislo)
                else:
                    if cislo in a_number and cislo not in cows:
                        #print("cow")
                        cows.append(cislo)
            #---Showing the result of each guessing       
            print(f"{len(bulls)} bulls, {len(cows)} cows")
            print(sline) 
            #---Showing the final result
            if len(bulls) == 4:
                print(f"Correct, you've guessed the right number in {guesses} guess!") if guesses == 1 else print(f"Correct, you've guessed the right number in {guesses} guesses!")
                if guesses < 4:
                    print("That`s amazing")
                elif guesses < 7:
                    print("Average score")
                else:
                    print("Not so good...")
                break
            else:
                continue
    #---Ending time counting
    end_time = time.time()
    print(time_format(start_time, end_time))
    date = datetime.datetime.now()
    fdate = date.strftime("%x")
    #---Writing score to score.txt file
    txt_file = open("score.txt", mode="a")
    txt_file.write(f"\nDatum: {fdate} | Guesses: {guesses} | {time_format(start_time, end_time)}")
    txt_file.close()
    #---Condition for continue
    guessing = input("Do you want to play again? (y/n): ")
    if guessing == "y":
        game_on = True
    else:
        game_on = False
print(sline + "\nThank you for your game\nBye!\n" + sline)    


