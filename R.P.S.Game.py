# Rock Paper Scissors Game
import random
L=['rock','paper','scissors']
C=random.choice(L)

U=(input("Enter any one of them Rock,Paper,Scissors : ")).lower()

if(U=='rock' or U=='paper' or U=='scissors'):
    if(C==U):
        print("Match is Draw")
        print("Computer has",C)
    elif(C=='rock' and U=='paper'):
        print("You Win the match")
        print("Computer has",C)
    elif(C=='rock' and U=='scissors'):
        print("You lost the match")
        print("Computer has",C)
    elif(C=='paper' and U=='rock'):
        print("You Win the match")
        print("Computer has",C)
    elif(C=='paper' and U=='scissors'):
        print("You lost the match")
        print("Computer has",C)
    elif(C=='scissors' and U=='paper'):
        print("You lost the match")
        print("Computer has",C)
    elif(C=='scissors' and U=='rock'):
        print("You Win the match")
        print("Computer has",C)
else:
    print("Invalid")    
