import random


class Mine_Sweeper:
    rows = 5
    columns = 5
    EMPTY = ""
    MINE = "X"  # Changed from emoji to letter
    HIDDEN = "■"  # Changed to a simpler block character
    MINE_COUNT = 5

    def __init__(self):
        self.grid = [[self.EMPTY for _ in range(self.columns)] for _ in range(self.rows)]
        self.visible = [[False for _ in range(self.columns)] for _ in range(self.rows)]

    def print_grid(self):
        # Print column headers - each centered in a 5-char wide cell
        print("   ", end="")
        for c in range(1, self.columns + 1):
            print(f"  {c}   ", end="")
        print()

        # Print top border
        print("  +" + "-----+" * self.columns)

        for r in range(self.rows):
            # Print row number
            print(f"{r + 1} |", end="")

            for c in range(self.columns):
                if self.visible[r][c]:
                    val = self.grid[r][c]
                    if val == self.MINE:
                        cell = f"  {self.MINE}  "
                    elif val == 0:
                        cell = "     "  # Empty space for 0
                    else:
                        cell = f"  {val}  "
                else:
                    cell = f"  {self.HIDDEN}  "

                print(f"{cell}|", end="")
            print()

            # Print row separator
            print("  +" + "-----+" * self.columns)
        print()

    def reveal(self, row, col):
        """Reveal a cell and flood-fill if it's empty (0 mines nearby)"""
        if not (0 <= row < self.rows and 0 <= col < self.columns):
            return

        if self.visible[row][col]:
            return

        if self.grid[row][col] == self.MINE:
            return

        self.visible[row][col] = True

        # If this cell has 0 adjacent mines, recursively reveal neighbors
        if self.grid[row][col] == 0:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    self.reveal(row + dr, col + dc)

    def is_move_valid(self, row, col) -> bool:
        return (
                0 <= row < self.rows and
                0 <= col < self.columns and
                not self.visible[row][col]
        )

    def is_mine(self, row, col) -> bool:
        return self.grid[row][col] == self.MINE

    def place_mines(self):
        placed = 0
        while placed < self.MINE_COUNT:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.columns - 1)
            if self.grid[r][c] != self.EMPTY:
                continue
            self.grid[r][c] = self.MINE
            placed += 1

    def count_neighbor_mines(self, row, col) -> int:
        count = 0

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < self.rows and 0 <= new_col < self.columns:
                    if self.grid[new_row][new_col] == self.MINE:
                        count += 1
        return count

    def fill_numbers(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.grid[r][c] == self.MINE:
                    continue
                count = self.count_neighbor_mines(r, c)
                self.grid[r][c] = count

    def all_safe_revealed(self) -> bool:
        """True if every non-mine cell is visible."""
        for r in range(self.rows):
            for c in range(self.columns):
                if self.grid[r][c] != self.MINE and not self.visible[r][c]:
                    return False
        return True