from ast import While, main
from asyncio.windows_events import NULL
from cgi import print_arguments
import random
import string
import csv
from xml.dom.minidom import Element

#Result counter variables
comp_wins = 0
player_wins = 0
ties = 0

#Function for player choice
def Choose_Option():
    while True: #While loop fixes bug of game results not being displayed when elif conditions not met
        user_choice = input("ROCK, PAPER, OR SCISSORS?: ")
        if len(user_choice) < 1: #Prevents crash if nothing is entered
            print("\nQUIT TRYING TO BREAK MY CODE. DO IT RIGHT THIS TIME.  ಠ╭╮ಠ\n")
        elif (user_choice.lower()[0] == "r"):
            user_choice = "r"
        elif (user_choice.lower()[0] == "p"):
            user_choice = "p"
        elif (user_choice.lower()[0] == "s"):
            user_choice = "s"
        else:
            print("\nQUIT TRYING TO BREAK MY CODE. DO IT RIGHT THIS TIME.  ಠ╭╮ಠ\n")
        return user_choice
    pass #Breaks out of while loop, goes to Play_Again()

#Function for computer choice
def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice

#Function for replay
def Play_Again():
    user_choice = input("PLAY AGAIN? (Y/N)")
    if len(user_choice) < 1: #Prevents crash if nothing is entered
        print("\nQUIT TRYING TO BREAK MY CODE. DO IT RIGHT THIS TIME.  ಠ╭╮ಠ\n")
        Play_Again()
    elif (user_choice.lower()[0] == "y"):
        return
    elif (user_choice.lower()[0] == "n"):
        print("\n***GOODBYE***\n")
        f = open("test_file.csv", "w", newline="") #'w' will overwrite the information in the file
        tup1 = ("Player Wins", player_wins)
        writer = csv.writer(f)
        writer.writerow(tup1)
        tup2 = ("Computer Wins", comp_wins)
        writer = csv.writer(f)
        writer.writerow(tup2)
        tup3 = ("Ties", ties)
        writer = csv.writer(f)
        writer.writerow(tup3)
        f.close()
        quit()
    else:
        print("\nQUIT TRYING TO BREAK MY CODE. DO IT RIGHT THIS TIME.  ಠ╭╮ಠ\n")
        Play_Again()

#First function called: a main menu of sorts
def Opening_Choice():
        user_choice = input("\n1 TO START GAME\n2 TO SEE PREVIOUS SCOREBOARD\n>>>")
        if user_choice == "1":
            print("\nLET'S GO:")
        elif user_choice == "2":
            file = open("test_file.csv", "r")
            data = list(csv.reader(file, delimiter=","))
            file.close()
            print(data)
            Opening_Choice()
        elif len(user_choice) < 1:
            print("\nQUIT TRYING TO BREAK MY CODE. DO IT RIGHT THIS TIME.  ಠ╭╮ಠ\n")
            Opening_Choice()
        else:
            print("\nQUIT TRYING TO BREAK MY CODE. DO IT RIGHT THIS TIME.  ಠ╭╮ಠ\n")
            Opening_Choice()


#Game or previous scores choice
print("********\nWELCOME:\n********")
Opening_Choice()

#Main method loop
while __name__ == "__main__":
    
    #Choice function calls 
    #Fixes bug by allowing a direct return to the Choose_Option function (fixes recursion problem)
    print("")
    user_choice = Choose_Option()
    while True:
        if len(user_choice) < 1: #Prevents crash on null values
            user_choice = Choose_Option()
        elif (user_choice.lower()[0] != "r" and user_choice.lower()[0] != "p" and user_choice.lower()[0] != "s"): #Handles str, int, and special exceptions
            user_choice = Choose_Option()
        else:
            break
    comp_choice = Computer_Option()
    print("")
    
    #Outcomes for games
    if user_choice == "r":
        if comp_choice == "r":
            print("****************\nRESULT:\nPLAY: ROCK\nCOMP: ROCK\nOUTC: TIE\n****************\n")
            ties += 1
        
        elif comp_choice == "p":
            print("****************\nRESULT:\nPLAY: ROCK\nCOMP: PAPER\nOUTC: LOSS\n****************\n")
            comp_wins += 1
            
        elif comp_choice == "s":
            print("****************\nRESULT:\nPLAY: ROCK\nCOMP: SCISSORS\nOUTC: WIN\n****************\n")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("****************\nRESULT:\nPLAY: PAPER\nCOMP: ROCK\nOUTC: WIN\n****************\n")
            player_wins += 1
        
        elif comp_choice == "p":
            print("****************\nRESULT:\nPLAY: PAPER\nCOMP: PAPER\nOUTC: TIE\n****************\n")
            ties += 1
            
        elif comp_choice == "s":
            print("****************\nRESULT:\nPLAY: PAPER\nCOMP: SCISSORS\nOUTC: LOSS\n****************\n")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("****************\nRESULT:\nPLAY: SCISSORS\nCOMP: ROCK\nOUTC: LOSS\n****************\n")
            comp_wins += 1
        
        elif comp_choice == "p":
            print("****************\nRESULT:\nPLAY: SCISSORS\nCOMP: PAPER\nOUTC: WIN\n****************\n")
            player_wins += 1
            
        elif comp_choice == "s":
            print("****************\nRESULT:\nPLAY: SCISSORS\nCOMP: SCISSORS\nOUTC: TIE\n****************\n")
            ties += 1

    #Scoreboard
    print("****************")
    print("PLAY WINS: " + str(player_wins))
    print("COMP WINS: " + str(comp_wins))
    print("TIES: " + str(ties))
    print("****************")
    
    #Replay function call
    Play_Again()
    #END OF LOOP
