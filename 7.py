def print_board(board):
  for row in board:
    print("|", end="")
    for cell in row:
      print(f"{cell} |", end="")
    print("\n-----------\n")

def check_win(board, player):
  # Check rows, columns, and diagonals for a win
  for row in board:
    if all(cell == player for cell in row):
      return True
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
    return True
  return False

def tic_tac_toe():
  board = [[' ', ' ', ' ']] * 3  # Create a list of lists for the board

  print_board(board)

  while True:
    player = 'X' if len([cell for row in board for cell in row if cell != ' ']) % 2 == 0 else 'O'  # Determine current player
    print(f"Player {player}'s turn.")

    row = int(input("Enter the row of your move (0-2): "))
    col = int(input("Enter the column of your move (0-2): "))

    if not (0 <= row <= 2 and 0 <= col <= 2) or board[row][col] != ' ':
      print("Invalid move. Please try again.")
      continue

    board[row][col] = player
    print_board(board)

    if check_win(board, player):
      print(f"Player {player} wins!")
      break

    if all(cell != ' ' for row in board for cell in row):  # Check for tie
      print("It's a tie!")
      break

# Add code to start the game (optional)
tic_tac_toe()
