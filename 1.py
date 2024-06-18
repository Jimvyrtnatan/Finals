import random

def guess(x):
  rand_number = random.randint(1, x)
  guess_count = 0
  while True:
    guess_num = int(input("Guess a number between 1 and " + str(x) + ": "))
    guess_count += 1
    if guess_num == rand_number:
      print("You guessed it! It took you " + str(guess_count) + " tries.")
      break
    elif guess_num < rand_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")

if __name__ == "__main__":
  guess(100)