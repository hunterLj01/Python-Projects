#MULTIPLE IF STATEMENTS PROGRAM PRACTICE
print("Welcome to the RollerCoaster Ride")
height=int(input("Enter Height (in cm): "))
if height<120:
  print("No Ticket")
else:
  age=int(input("Enter Age :"))
  if age<18:
    photo=int(input("Do you want a photo? 1 or 0 : "))
    if photo == 1:
      print("Your Net bill would be : $3 + $7 = $10")
      #Multiple if statements
    else:
      print("Your bill would be $7 ")
  elif age>18:
    photo=int(input("Do you want a photo? 1 or 0 : "))
    if photo == 1:
      print("Your Net bill would be : $3 + $12 = $15")
    else:
      print("Your bill would be $12 ")
  
