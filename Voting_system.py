#   Voting System
age = int(input("enter your age : "))
if (age>=18):
  print("Welcome , You are Eligible for voting")
  cho = int(input("""Enter your choice no. 
       1 -> ABC
       2 -> EFGH
       3 -> XYZ 
       4 -> PQR
       """))
  if (cho == 1):
    print("congratulation you vote for ABC")
  elif (cho == 2):
    print("congratulation you vote for EFGH")
  elif (cho == 3):
    print("congratulation you vote for XYZ")
  elif (cho == 4):
    print("congratulation you vote for PQR")
  else:
    print("Invalid")
else:
  print("SORRY , You are not Eligible for voting")  
