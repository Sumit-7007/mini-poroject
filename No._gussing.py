#  Number gussing game
import random
C= random.randint(1,50)
I= int(input("Enter the No. choose by computer : "))
D=abs(C-I)
if C==I:
    print("Congratulations, you win the game\nNo. choose by computer is",C)
else:
    print("You lost the game\nNo. choose by computer is",C)
    if (D== 1 or D==2 or D==3):
        print("You are very close")
