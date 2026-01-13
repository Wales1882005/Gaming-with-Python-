import random

# Create the board
def create_board():
    return [" " for _ in range(9)]

# Show board with position numbers
def print_board_with_positions(board):
    for i in range(3):
        row = []
        for j in range(3):
            index = i * 3 + j
            cell = board[index] if board[index] != " " else str(index + 1)
            row.append(cell)
        print("|".join(row))
        if i < 2:
            print("-" * 5)

# Player move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Choose a number between 1 and 9.")
            elif board[move] != " ":
                print("That spot is taken.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Invalid input. Enter a number.")

# Easy AI: random move
def computer_easy(board):
    empty_spots = [i for i, cell in enumerate(board) if cell == " "]
    move = random.choice(empty_spots)
    board[move] = "O"
    print(f"Computer chooses position {move + 1} (Easy)")

# Medium AI: block player if needed
def computer_medium(board):
    empty_spots = [i for i, cell in enumerate(board) if cell == " "]

    # Try to block player
    for move in empty_spots:
        board_copy = board.copy()
        board_copy[move] = "X"
        if check_win(board_copy, "X"):
            board[move] = "O"
            print(f"Computer blocks at position {move + 1} (Medium)")
            return

    # Else random
    move = random.choice(empty_spots)
    board[move] = "O"
    print(f"Computer chooses position {move + 1} (Medium)")

# Check win
def check_win(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Check draw
def check_draw(board):
    return " " not in board

# Game loop: Player vs Player
def play_pvp():
    board = create_board()
    current_player = "X"
    while True:
        print_board_with_positions(board)
        player_move(board, current_player)
        if check_win(board, current_player):
            print_board_with_positions(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board_with_positions(board)
            print("🤝 It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

# Game loop: Player vs Computer
def play_vs_computer(difficulty):
    board = create_board()
    while True:
        print_board_with_positions(board)
        player_move(board, "X")
        if check_win(board, "X"):
            print_board_with_positions(board)
            print("🎉 You win!")
            break
        elif check_draw(board):
            print_board_with_positions(board)
            print("🤝 It's a draw!")
            break

        # Computer move based on difficulty
        if difficulty == "easy":
            computer_easy(board)
        elif difficulty == "medium":
            computer_medium(board)

        if check_win(board, "O"):
            print_board_with_positions(board)
            print("💻 Computer wins!")
            break
        elif check_draw(board):
            print_board_with_positions(board)
            print("🤝 It's a draw!")
            break

# Main menu
def main():
    print("🎮 Welcome to Tic-Tac-Toe!")
    print("1. Play against another player")
    print("2. Play against computer")
    choice = input("Choose option (1 or 2): ")

    if choice == "1":
        play_pvp()
    elif choice == "2":
        print("Choose difficulty:")
        print("a. Easy")
        print("b. Medium")
        diff_choice = input("Enter a or b: ").lower()
        if diff_choice == "a":
            play_vs_computer("easy")
        elif diff_choice == "b":
            play_vs_computer("medium")
        else:
            print("Invalid difficulty choice.")
    else:
        print("Invalid menu choice.")

main()
