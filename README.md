# Connect-4 with MCTS Bot

A Python implementation of the classic Connect-4 game featuring an AI opponent powered by the Monte Carlo Tree Search (MCTS) algorithm.

## 🎮 Game Overview

Connect-4 is a two-player strategy game where players take turns dropping colored tokens into a 6x7 grid. The objective is to be the first to connect four tokens horizontally, vertically, or diagonally.

**Features:**
- Human vs AI gameplay
- MCTS-powered intelligent bot opponent
- Console-based interface with visual board display
- Win tracking across multiple games
- Comprehensive win detection (horizontal, vertical, diagonal)

## 🤖 AI Implementation

The bot uses **Monte Carlo Tree Search (MCTS)**, a powerful algorithm that combines:

- **Selection**: Uses UCB1 (Upper Confidence Bound) formula to balance exploration vs exploitation
- **Expansion**: Generates all possible moves from current game state
- **Simulation**: Runs random playouts to terminal states
- **Backpropagation**: Updates node statistics based on simulation results

The AI performs **1000 MCTS iterations** per move, providing challenging and strategic gameplay.

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- NumPy

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/al-Jurjani/Connect-4-with-MCTS-Bot.git
   cd Connect-4-with-MCTS-Bot
   ```

2. Install required dependencies:
   ```bash
   pip install numpy
   ```

### Running the Game

```bash
python connect4.py
```

## 🎯 How to Play

1. The game starts with an empty 6x7 grid
2. **Player 1 (Human)**: Uses 'O' tokens - goes second
3. **Bot**: Uses 'X' tokens - goes first
4. Enter column numbers 1-7 when prompted
5. First to connect four tokens wins!

### Game Flow:
- Bot makes the first move automatically
- Human player chooses columns via console input
- Board updates and displays after each move
- Game announces winner or draw
- Option to play again after each game

## 📁 Project Structure

```
Connect-4-with-MCTS-Bot/
├── connect4.py         # Main game loop and user interface
├── Board.py           # Board class with game logic and state management
├── monteCarlo.py      # MCTS algorithm implementation
└── README.md         # Project documentation
```

## 🔧 Code Architecture

### `Board.py`
- **Board representation**: 6x7 NumPy array
- **Game state management**: Track remaining slots, column heights
- **Win detection**: Horizontal, vertical, and diagonal checking
- **Move validation**: Ensure valid column selections
- **Deep copy support**: For MCTS tree exploration

### `connect4.py`
- **Game loop**: Alternates between human and bot turns
- **User interface**: Console-based input/output
- **Score tracking**: Maintains win counts across games
- **Game flow control**: Handles game restart and termination

### `monteCarlo.py`
- **MCTS implementation**: Complete tree search algorithm
- **Node class**: Represents game states in search tree
- **UCB1 selection**: Balances exploration and exploitation
- **Random simulations**: Plays out games to completion
- **Statistics tracking**: Win rates and visit counts

## ⚙️ Configuration

### MCTS Parameters

You can modify these values in `monteCarlo.py`:

```python
# Number of MCTS iterations per move (line 16 in search method)
for i in range(1000):  # Increase for stronger AI, decrease for faster moves

# UCB1 exploration parameter
EXPLORATION_PARAMETER = math.sqrt(2)  # Default: √2 ≈ 1.414
```

### Performance Tuning

- **Iterations**: 1000 (current) - provides strong gameplay
- **Higher values**: Stronger AI but slower moves
- **Lower values**: Faster moves but weaker AI

## 🎮 Gameplay Features

### Board Display
```
    1     2    3    4    5    6    7   
  ____________________________________
1 |   |   |   |   |   |   |   | 
2 |   |   |   |   |   |   |   | 
3 |   |   |   |   |   |   |   | 
4 |   | X | X | O |   |   |   | 
5 | X | X | O | O |   |   |   | 
6 | X | O | O | O | X |   |   | 
  ____________________________________
```

### Input Validation
- Validates column range (1-7)
- Prevents moves in full columns
- Handles invalid input gracefully
- Provides clear error messages

### Win Detection
- **Horizontal**: 4 consecutive tokens in any row
- **Vertical**: 4 consecutive tokens in any column  
- **Diagonal**: 4 consecutive tokens in any diagonal direction
- **Draw**: All 42 slots filled without a winner

## 🔬 MCTS Algorithm Details

### UCB1 Formula
```
UCB1 = (wins/visits) + c * √(ln(parent_visits)/visits)
```
Where `c = √2` (exploration parameter)

### Search Process
1. **1000 iterations** of MCTS per move
2. **Selection**: Navigate tree using UCB1
3. **Expansion**: Add all possible moves as child nodes
4. **Simulation**: Random playout from selected node
5. **Backpropagation**: Update win/visit statistics
6. **Best move**: Select child with highest win rate

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- **GUI Implementation**: Add graphical interface
- **Difficulty Levels**: Configurable AI strength
- **Performance Optimization**: Speed up MCTS search
- **Additional Features**: Move history, game analysis
- **Code Refactoring**: Improve structure and documentation

## 📈 Performance

- **Search Depth**: Varies based on game state
- **Move Time**: ~1-3 seconds per bot move
- **Memory Usage**: Minimal, cleans up search tree between moves
- **AI Strength**: Challenging for most human players

## 🐛 Known Issues

- Bot always goes first (X tokens)
- No save/load game functionality  
- Console-only interface
- Fixed MCTS iteration count

## 📄 License

This project is open source. Feel free to use and modify.

## 👤 Author

**al-Jurjani**
- GitHub: [@al-Jurjani](https://github.com/al-Jurjani)

---

**Challenge the AI and test your Connect-4 skills! 🎯**