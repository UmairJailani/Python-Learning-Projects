import random

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

options = [rock, paper, scissors]

player_choice = int(input("Choose between 0 for Rocks, 1 for Paper & 2 for Scissors!\n"))

print("The Player Choose")
print(options[player_choice])

a_choice = random.randint(0,2)
print("The Computer Choose")
print(options[a_choice])

if a_choice == 0 and player_choice == 0:
    print("Its a draw")
elif a_choice == 0 and player_choice == 1:
    print("The Player Wins")
elif a_choice == 0 and player_choice == 2:
    print("The Computer Wins")
elif a_choice == 1 and player_choice == 0:
    print("The Computer Wins")
elif a_choice == 1 and player_choice == 1:
    print("Its a draw")
elif a_choice == 1 and player_choice == 2:
    print("The Player Wins")
elif a_choice == 2 and player_choice == 0:
    print("The Player Wins")
elif a_choice == 2 and player_choice == 1:
    print("The Computer Wins")
elif a_choice == 2 and player_choice == 2:
    print("Its a draw")
else:
    print("You Choose Wrong.")