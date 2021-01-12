##import the module random
import random

##DICES
##returns a random integer between (1,6) x2
dice1=random.randint(1,6)
dice1=int(dice1)
dice2=random.randint(1,6)
dice2=int(dice2)
dice=int(dice1)+int(dice2)

##TOTAL NUMBER OF PLAYS
i=0

##GAME STARTS HERE
##user input roll
roll=input("Welcome to Craps! Type ROLL to begin: ").upper()
roll=str(roll)


##if roll is a string
while roll==roll:
    ##if user types "QUIT", print terminate message and 'break' the game
    if roll=="QUIT":
        print("You have terminated the game!")
        break
    ##if user types "ROLL", print the 2 random dice numbers
    elif roll=="ROLL":
        print(str(dice1) + ":" + str(dice2))
        ##if dice total rolls 7 or 11 print win and total games played and break the game 
        if dice==7 or dice==11:
            print("Total of both dices is: " + str(dice))
            print("Congrats! You Won!!!")
            print("Total number of round played: " + str(i+1))
            break
        ##if dice total rolls 2, 3 or 12 print lose and total games played and break the game
        elif dice==2 or dice==3 or dice==12:
            print("Total of both dices is: " + str(dice))
            print("CRAPS!!! Sorry... You Lost!!!")
            print("Total number of round played: " + str(i+1))
            break
        ##if other numbers, print try again and let user input roll again (add 1 play to i)
        else:
            print("Total of both dices is: " + str(dice))
            i=i+1
    ##if other string, print error and let user input roll again
    else:
        print("Error!!! TYPO!! Please type ROLL or QUIT")
    ##roll input for the whole loop
    roll=input("Please try again! Type ROLL: ").upper()
    roll=str(roll)
    dice1=random.randint(1,6)
    dice1=int(dice1)
    dice2=random.randint(1,6)
    dice2=int(dice2)
    dice=int(dice1)+int(dice2)
    



