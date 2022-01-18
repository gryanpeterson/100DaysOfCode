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

print("Welcome to the Rock, Paper, Scissors game! \n")
player_selection = int(input("Enter 0 for Rock, 1 for Paper or 2 for Scissors. "))
choices = [0, 1, 2]
computer_play = random.choice(choices)

if player_selection == 0 and computer_play == 2:
  print(f"{rock} \n Computer chose: {scissors} \n You win! ")
elif player_selection == 1 and computer_play == 0:
  print(f"{paper} \n Computer chose: {rock} \n You win! ")
elif player_selection == 2 and computer_play == 1:
  print(f"{scissors} \n Computer chose: {paper} \n You win! ")
elif player_selection == 0 and computer_play == 1:
  print(f"{rock} \n Computer chose: {paper} \n You lose! ")
elif player_selection == 1 and computer_play == 2:
  print(f"{paper} \n Computer chose: {scissors} \n You lose! ")
elif player_selection == 2 and computer_play == 0:
  print(f"{scissors} \n Computer chose: {rock} \n You lose! ")
elif player_selection == 0 and computer_play == 0:
  print(f"{rock} \n Computer chose: {rock} \n Tie! You both chose Rock! ")
elif player_selection == 1 and computer_play == 1:
  print(f"{paper} \n Computer chose: {paper} \n Tie! You both chose Paper! ")
elif player_selection == 2 and computer_play == 2:
  print(f"{scissors} \n Computer chose: {scissors} \n Tie! You both chose Scissors! ")
