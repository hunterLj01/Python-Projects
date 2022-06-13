rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

u_choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. :\n "))

if u_choose >=3:
  print("Not a valid option, Choose again!")
elif u_choose == 0:
  print(rock)
elif u_choose == 1 :
  print(paper)
elif u_choose == 2 :
  print(scissors)
else:
  

 ''' 
 this could alternatively be done by using 'lists'
 game_image=['rock', 'paper', 'scissors']
 #for user
 print(game_image[u_choose])
 #for computer
 #after the random. randomint input
 print(game_image[comp_choose])

 #catch!
 in case of number>=3 lists will throw the index out of range error
 '''


comp_choose=random.randint(0,2)

if comp_choose == 0:
  print(f"Computer chose {rock}")
elif comp_choose == 1 :
  print(f"Computer chose {paper}")
elif comp_choose == 2 :
  print(f"Computer chose {scissors}")

if u_choose == comp_choose:
  print("Its a DRAW!") 
elif (u_choose == 0 and comp_choose==1) or (u_choose == 1 and comp_choose==2) or (u_choose == 2 and comp_choose== 0):
  print("You Loose!")
elif (u_choose == 1 and comp_choose== 0) or (u_choose == 2 and comp_choose==1) or (u_choose == 0 and comp_choose== 2):
  print("You Win!")

