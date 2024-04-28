#  Number System
S=int(input("Enter the starting point : "))
E=int(input("Enter the ending point : "))
A=int(input("Enter the apdation point : "))
FR=input("Enter choice for print Forward / Reverse : ").lower()

if (FR == 'forward'  ) :
  RC=input("Enter choice for print Row / Column : ").lower()
  for i in range (S,E+1,A):
      if (RC == 'column'):
        print(i)
      elif (RC == 'row'):
        print(i, end =" ")
      else :
        print("invalid")
        break
elif (FR == 'reverse' ) :
  RC=input("Enter choice for print Row / Column : ").lower()
  for i in range (E,S-1,-A) :
      if (RC == 'column'):
        print(i)
      elif (RC == 'row'):
        print(i, end =" ")
      else :
        print("Invalid")
        break

else :
  print("Invalid")
  






