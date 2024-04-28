#    Grading System
Max = int(input("Enter maximum marks : "))
Obt = float(input("Enter obtained marks : "))
Per=(Obt/Max)*100
if(Max<Obt):
  print("Invalid")
#print("percentage = ""%.2f"%Per,"%")
#print("percentage = ",round(Per,2),"%")
elif(Per==100):
  print("Congratulation you got  A++ Grade ")
elif( 100>Per>=90):
  print("Congratulation you got  A+ Grade ")
elif( 90>Per>=80):
  print("Congratulation you got  A Grade ")
elif( 80>Per>=70):
  print("Congratulation you got  B+ Grade ")
elif( 70>Per>=60):
  print("Congratulation you got  B Grade ")
elif( 60>Per>=50):
  print("Congratulation you got  C+ Grade ")
elif( 50>Per>=40):
  print("Congratulation you got  C Grade ")
elif( 40>Per>=30):
  print("Congratulation you got  D Grade ")
else:
  print("You are Fail \nYou got  F Grade ")
