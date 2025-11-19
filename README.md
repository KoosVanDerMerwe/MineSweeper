# 💣 Minesweeper

A classic Minesweeper game built in Python with a clean terminal interface.

## 📋 Description

This is a text-based implementation of the classic Minesweeper puzzle game. Players reveal cells on a 5x5 grid, trying to avoid hidden mines while using number clues to deduce mine locations. The game features automatic flood-fill revealing for empty cells, making gameplay smooth and intuitive.

## ✨ Features

- **5x5 Grid**: Compact game board perfect for quick sessions
- **5 Hidden Mines**: Balanced difficulty for beginners
- **Smart Flood-Fill**: Automatically reveals connected empty cells when you click a zero
- **Number Clues**: Shows how many mines are adjacent to each revealed cell
- **Clean Grid Display**: Professional table layout with row/column labels
- **Input Validation**: Prevents invalid moves and handles errors gracefully

## 🎮 How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Enter coordinates to reveal cells:
   - Row number (1-5)
   - Column number (1-5)

3. **Win Condition**: Reveal all safe cells without hitting a mine
4. **Lose Condition**: Click on a mine - game over!

### Game Symbols
- `■` - Hidden cell (not yet revealed)
- `1-8` - Number indicating adjacent mines
- `X` - Mine (shown when you lose)
- Empty space - No adjacent mines

## 📸 Screenshots

### Starting Grid
```
      1     2     3     4     5  
  +-----+-----+-----+-----+-----+
1 |  ■  |  ■  |  ■  |  ■  |  ■  |
  +-----+-----+-----+-----+-----+
2 |  ■  |  ■  |  ■  |  ■  |  ■  |
  +-----+-----+-----+-----+-----+
3 |  ■  |  ■  |  ■  |  ■  |  ■  |
  +-----+-----+-----+-----+-----+
4 |  ■  |  ■  |  ■  |  ■  |  ■  |
  +-----+-----+-----+-----+-----+
5 |  ■  |  ■  |  ■  |  ■  |  ■  |
  +-----+-----+-----+-----+-----+
```

### Mid-Game
```
      1     2     3     4     5  
  +-----+-----+-----+-----+-----+
1 |  1  |  2  |  1  |  1  |     |
  +-----+-----+-----+-----+-----+
2 |     |  1  |  1  |  ■  |  ■  |
  +-----+-----+-----+-----+-----+
3 |     |  1  |  2  |  ■  |  ■  |
  +-----+-----+-----+-----+-----+
4 |  1  |  2  |  2  |  2  |  1  |
  +-----+-----+-----+-----+-----+
5 |     |     |     |  1  |  ■  |
  +-----+-----+-----+-----+-----+
```

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone or download this repository
2. Ensure you have both files in the same directory:
   - `main.py` - Main game loop
   - `mine_sweeper.py` - Game logic and Mine_Sweeper class

3. Run the game:
   ```bash
   python main.py
   ```

No external dependencies required - uses only Python standard library!

## 📂 Project Structure

```
minesweeper/
├── main.py           # Game loop and user interface
├── mine_sweeper.py   # Mine_Sweeper class (game logic)
└── README.md         # This file
```

## 🧩 Code Highlights

### Key Features Implemented

**Flood-Fill Algorithm**
```python
def reveal(self, row, col):
    """Recursively reveals connected empty cells"""
    if self.grid[row][col] == 0:
        # Automatically reveal all adjacent cells
```

**Mine Placement**
```python
def place_mines(self):
    """Randomly places mines without overlapping"""
```

**Win Detection**
```python
def all_safe_revealed(self):
    """Checks if all non-mine cells are visible"""
```

## 🎓 What I Learned

Building this project taught me:
- **2D Arrays**: Managing grid-based data structures
- **Recursion**: Implementing flood-fill algorithm
- **OOP Design**: Separating game logic from UI
- **Input Validation**: Handling edge cases and errors
- **State Management**: Tracking visible vs hidden cells

## 🚀 Future Enhancements

Potential features to add:
- [ ] Flag system to mark suspected mines
- [ ] Difficulty levels (Easy/Medium/Hard)
- [ ] Timer to track completion time
- [ ] High score system with file persistence
- [ ] First-click safety guarantee
- [ ] Chord clicking (reveal neighbors when flags match)
- [ ] Undo move functionality
- [ ] Custom grid sizes

## 🤝 Contributing

This is a learning project, but suggestions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Share improvements

## 📝 License

Free to use for learning purposes. Do whatever you want with it!

## 👤 Author

*signed: Nic (Koos) – 19/11/2025* ✍️

---

**Enjoy the game, and watch out for those mines!** 💣
