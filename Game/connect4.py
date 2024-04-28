import numpy as np
class connect4:
    redWins = 0
    yellowWins = 0
    board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']])
    
    def __init__(self) -> None:
        pass

    def playGame(self):
        col = -1
        row = -1
        height = np.array([6, 6, 6, 6, 6, 6, 6])
        slotsRemaining = 42
        curPlayer = ' '
        while(slotsRemaining > 0):
            self.printBoard()
            curPlayer = self.curPlayer(slotsRemaining)
            col = self.colPos(height)
            row = self.enterToken(col, height, curPlayer)
            print(row)
            slotsRemaining -= 1

            if self.checkVer(col, curPlayer) | self.checkHor(row, curPlayer) | self.checkDiag(row, col, curPlayer):
                self.printBoard()
                print("Player '" + curPlayer + "' has won!")
                if curPlayer == 'X':
                    self.redWins += 1
                else:
                    self.yellowWins += 1
                slotsRemaining, height = self.playAgain()
            elif (slotsRemaining == 0):
                print("All slots filled! Game drawn!")
                slotsRemaining, height = self.playAgain()

    def curPlayer(self, slotsRemaining):
        if slotsRemaining % 2 == 0:
            print("Player 1's turn. Token = 'X'")
            return 'X'
        else:
            print("Player 2's turn. Token = 'O'")
            return 'O'

    def colPos(self, height):
        try:
            col = int(input("Choose what column to insert your token in: 1-7\n")) - 1
            if col < 0 or col > 6:
                print("Please enter a number between 1 and 7.")
                return self.colPos()
            if height[col] == 0:
                print("The column is already full! Enter into another column!")
                return self.colPos()
            return col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            return self.colPos()

    def enterToken(self, col, height, curPlayer):
        height[col] -= 1
        self.board[height[col]][col] = curPlayer
        return height[col]

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

    def playAgain(self):
        response = input("Do you want to play again? (y/n)\n")
        if response.lower() in {'y', 'yes', 'ok', 'okay', 'k'}:
            self.initBoard()
            return 42, np.array([6, 6, 6, 6, 6, 6, 6])
        elif response.lower() in {'n', 'no', 'na', 'nop', 'nope'}:
            print("Red's total wins: " + str(self.redWins))
            print("Yellow's total wins: " + str(self.yellowWins))
            return 0, np.array([6, 6, 6, 6, 6, 6, 6])

    def initBoard(self):
        self.board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']])

    def printBoard(self):
        print("    1     2    3    4    5    6    7   ")
        print("  ____________________________________")
        for i in range(0, 6):
            print(str((i + 1)) + " |", end = ' ')
            for j in range(0, 7):
                print(" " + self.board[i][j] + " |", end = ' ')
            print()
        print("  ____________________________________\n\n")

game = connect4()
game.playGame()
