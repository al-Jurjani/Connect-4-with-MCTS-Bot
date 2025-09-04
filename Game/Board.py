import numpy as np

class Board:
    board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']])
    height = np.array([6, 6, 6, 6, 6, 6, 6])
    slotsRemaining = 42
    gameFinished = False

    def __init__(self) -> None:
        pass

    def initBoard(self):
        self.board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        self.height = np.array([6, 6, 6, 6, 6, 6, 6])
        self.slotsRemaining = 42
        self.gameFinished = False

    def curPlayer(self):
        if self.slotsRemaining == 0:
            self.gameFinished = True
            print("All slots Filled. Game Drawn!")
        elif self.slotsRemaining % 2 == 0:
            print("Player 1's turn. Token = 'X'")
            print("Slots Remaining: " + str(self.slotsRemaining))
            return 'X'
        else:
            print("Player 2's turn. Token = 'O'")
            print("Slots Remaining: " + str(self.slotsRemaining))
            return 'O'

    def curPlayerBot(self):
        if self.slotsRemaining == 0:
            self.gameFinished = True
            print("All slots Filled. Game Drawn!")
        elif self.slotsRemaining % 2 == 0:
            # print("Player 1's turn. Token = 'X'")
            # print("Slots Remaining: " + str(self.slotsRemaining))
            return 'X'
        else:
            # print("Player 2's turn. Token = 'O'")
            # print("Slots Remaining: " + str(self.slotsRemaining))
            return 'O'
    
    def colPos(self):
        try:
            col = int(input("Choose what column to insert your token in: 1-7\n")) - 1
            if col < 0 or col > 6:
                print("Please enter a number between 1 and 7.")
                return self.colPos()
            if self.height[col] == 0:
                print("The column is already full! Enter into another column!")
                return self.colPos()
            return col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            return self.colPos()

    def updateBoard(self, col, token):
        self.height[col] -= 1
        self.board[self.height[col]][col] = token
        self.slotsRemaining -= 1
        if self.slotsRemaining == 0:
            self.gameFinished = True

    def checkVer(self, col, curPlayer):
        for i in range(0, 3):
            if self.board[i][col] == curPlayer and self.board[i+1][col] == curPlayer and self.board[i+2][col] == curPlayer and self.board[i+3][col] == curPlayer:
                self.gameFinished = True
                return True
        return False

    def checkHor(self, row, curPlayer):
        for i in range(0, 3):
            if self.board[row][i] == curPlayer and self.board[row][i+1] == curPlayer and self.board[row][i+2] == curPlayer and self.board[row][i+3] == curPlayer:
                self.gameFinished = True
                return True
        return False

    def checkDiag(self, row, col, curPlayer):
        # Define directions for diagonal checking
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        # Check each direction
        for d in directions:
            count = 1  # Initialize count for consecutive tokens
            # Check tokens in the diagonal direction
            for i in range(1, 4):  # Check up to 3 tokens away from the current position
                # Calculate new position
                new_col = col + i * d[0]
                new_row = row + i * d[1]
                # Check if new position is within the board boundaries
                if 0 <= new_col < len(self.board[0]) and 0 <= new_row < len(self.board):
                    # Check if the token in the new position is the same as the current token
                    if self.board[new_row][new_col] == self.board[row][col] == curPlayer:
                        count += 1
                    else:
                        break  # Break if the consecutive streak is broken
                else:
                    break  # Break if the new position is out of bounds
            # Check if we have a winner
            if count >= 4:
                self.gameFinished = True
                return True  # Return True if there are 4 or more consecutive tokens in a diagonal direction
        return False  # Return False if no diagonal win is found

    def twoPlayer(self):
        response = input("Do you want to play against a player or bot?")
        if response.lower() in {'p', 'Player'}:
            return True
        elif response.lower() in {'b', 'bot'}:
            return False
    
    def goFirst(self):
        response = input("Who goes first? Red or Yellow")
        if response.lower() in {'r', 'red'}:
            return True
        elif response.lower() in {'y', 'yellow'}:
            return False

    def playAgain(self):
        response = input("Do you want to play again? (y/n)\n")
        if response.lower() in {'y', 'yes', 'ok', 'okay', 'k'}:
            self.initBoard()
            return 42, np.array([6, 6, 6, 6, 6, 6, 6])
        elif response.lower() in {'n', 'no', 'na', 'nop', 'nope'}:
            # print("Red's total wins: " + str(self.redWins))
            # print("Yellow's total wins: " + str(self.yellowWins))
            self.slotsRemaining = 0

    def checkFour(self, row, col, curPlayer):
        return self.checkHor(row, curPlayer) | self.checkVer(col, curPlayer) | self.checkDiag(row, col, curPlayer)

    def printBoard(self):
        print("    1     2    3    4    5    6    7   ")
        print("  ____________________________________")
        for i in range(0, 6):
            print(str((i + 1)) + " |", end = ' ')
            for j in range(0, 7):
                print(" " + self.board[i][j] + " |", end = ' ')
            print()
        print("  ____________________________________\n\n")

    # Following Methods for AI Bots
    def listOfMoves(self):
        moves = []
        for i in range(0, 7):
            if self.height[i] > 0:
                moves.append(i)
        return moves

    def __deepcopy__(self, memo):
        new_board = Board()
        new_board.board = np.copy(self.board)  # Ensure a true deep copy of the array
        new_board.height = np.copy(self.height)  # Ensure a true deep copy of the array
        new_board.slotsRemaining = self.slotsRemaining
        new_board.gameFinished = self.gameFinished
        return new_board