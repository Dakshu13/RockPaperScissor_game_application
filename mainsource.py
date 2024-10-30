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

game_choices = [rock, paper, scissors]
#Welcome all to your rock,paper and scissors gaming application!
print("Welcome to rock paper scissor game!")
#ask input from the user to choose a number and print the image respective to the number
user_choice = int(input("Enter the number ? 0 for Rock, 1 for paper and 2 for scissors"))
print(game_choices[user_choice])

# give computer to random give a number,i mean rock or paper or scissors with images respective to the number
computer_choice = random.randint(0,2)
print(f"Computer choice is :{computer_choice}")
print(game_choices[computer_choice])

#provide the conditions respective to the game such as
# 0 - rock and 1 - paper, so basically paper wins!
# remember, to provide the first condition, i.e. if the user choice is 3 and above and computer choice is below 0, then
# then, it's a invalid game!
if user_choice >= 3 or user_choice < 0:
    print("Invalid number!, you lost!")
elif user_choice == 0 and computer_choice == 1:
    print("Computer wins!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer wins!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")





