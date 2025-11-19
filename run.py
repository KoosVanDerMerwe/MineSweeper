from mine_sweeper import Mine_Sweeper

def main():
    play()

def play():
    board = Mine_Sweeper()
    board.place_mines()
    board.fill_numbers()

    print("Welcome to Mine Sweeper!")
    print("-" * 24)
    board.print_grid()

    while True:
        try:
            row_raw = int(input("Enter row number (1-5): "))
            col_raw = int(input("Enter column number (1-5): "))
            print()
        except ValueError:
            print("Please enter numbers only.\n")
            continue

        row = row_raw - 1
        col = col_raw - 1

        if not board.is_move_valid(row, col):
            print("Invalid move. Please try again.\n")
            continue

        if board.is_mine(row, col):
            for r in range(board.rows):
                for c in range(board.columns):
                    board.visible[r][c] = True
            board.print_grid()
            print("You lose! Game over.")
            break

        board.reveal(row, col)
        board.print_grid()

        if board.all_safe_revealed():
            print("You win! Congratulations!")
            break

if __name__ == "__main__":
    main()