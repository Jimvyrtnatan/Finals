import random

def play():
  user_choice = input("Choose Rock (r), Paper (p), or Scissors (s): ")
  computer_choice = random.choice(['r', 'p', 's'])
  
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == 'r' and computer_choice == 's':
    print("You win!")
  elif user_choice == 'p' and computer_choice == 'r':
    print("You win!")
  elif user_choice == 's' and computer_choice == 'p':
    print("You win!")
  else:
    print("You lose.")

if __name__ == "__main__":
  play()