import random

def dice_rolling_simulator():
  print("Dice Rolling Simulator")
  print("------------------")

  while True:
    num_players = input("Enter the number of players (2 or more, or 'q' to quit): ")
    if num_players.lower() == 'q':  # Handle 'q' in any case
      break

    try:
      num_players = int(num_players)
      if num_players < 2:
        print("Invalid number of players. Please enter 2 or more players.")
      else:
        # Rest of the code for handling players and rolling dice
        player_names = input("Enter the names of the players (separated by commas): ")
        player_names = [name.strip() for name in player_names.split(",")]
        print(f"Players: {', '.join(player_names)}")

        while True:
          player_turn = input(f"Enter the name of the player whose turn it is ({', '.join(player_names)}), or 'q' to quit: ")
          if player_turn.lower() == 'q':
            break

          if player_turn not in player_names:
            print("Invalid player. Please try again.")
          else:
            roll = random.randint(1, 6)
            print(f"{player_turn} rolled a {roll}!")
    except ValueError:
      print("Invalid input. Please enter a number of players.")

  print("\nThank you for using the Dice Rolling Simulator!")

dice_rolling_simulator()
