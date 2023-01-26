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
player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

if player_choice == 0:
  print(rock)
elif player_choice == 1:
  print(paper)
elif player_choice == 2:
  print(scissors)
else:
  print("This is not an option.")

computer_choice = random.randint(0, 2)
print(f"Computer's choice is {computer_choice}")

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
  


if player_choice == computer_choice:
  print("You draw.")
elif player_choice == 0 and computer_choice == 1:
  print("You  lose.")
elif player_choice == 0 and computer_choice == 2:
  print("You win.")
elif computer_choice == 0 and player_choice == 1:
  print("You win.")
elif computer_choice == 0 and player_choice == 2:
  print("You lose.")
elif player_choice == 1 and computer_choice == 2:
  print("You lose.")
elif player_choice == 2 and computer_choice == 1:
  print("You win")
else:
  print("This is not an option.")
