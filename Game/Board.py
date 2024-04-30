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
    
    def updateBoard(self, col, token):
        self.height[col] -= 1
        self.board[self.height[col]][col] = token
        self.slotsRemaining -= 1
    
    def checkVer(self, col, curPlayer):
        for i in range(0, 3):
            if self.board[i][col] == curPlayer and self.board[i+1][col] == curPlayer and self.board[i+2][col] == curPlayer and self.board[i+3][col] == curPlayer:
                return True
        return False
    
    def checkHor(self, row, curPlayer):
        for i in range(0, 3):
            if self.board[row][i] == curPlayer and self.board[row][i+1] == curPlayer and self.board[row][i+2] == curPlayer and self.board[row][i+3] == curPlayer:
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
                print("true")
                return True  # Return True if there are 4 or more consecutive tokens in a diagonal direction
        print("false")
        return False  # Return False if no diagonal win is found

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
    def listOfMoves(self, height):
        moves = list
        for i in range(0, 6):
            if height[i] > 0:
                moves.append(i)
        return moves