import numpy as np
class connect4:
    redWins = 0
    yellowWins = 0
    playAgain = 'y'
    slotsRemaining = 42
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
        curPlayer = ' '
        while(self.slotsRemaining > 0):
            self.printBoard()
            curPlayer = self.curPlayer()
            col = self.colPos()
            row = self.enterToken(col, curPlayer)
            self.slotsRemaining -= 1

            if self.checkVer(col, curPlayer) | self.checkHor(row, curPlayer):
                print("Player '" + curPlayer + "' has won!")
                if curPlayer == 'X':
                    self.redWins += 1
                else:
                    self.yellowWins += 1
                self.playAgain()
            elif (self.slotsRemaining == 0):
                print("All slots filled! Game drawn!")
                self.playAgain()

    def curPlayer(self):
        if self.slotsRemaining % 2 == 0:
            print("Player 1's turn. Token = 'X'")
            return 'X'
        else:
            print("Player 1's turn. Token = 'O'")
            return 'O'
    
    def colPos(self):
        try:
            col = int(input("Choose what column to insert your token in: 1-7\n")) - 1
            if col < 0 or col > 6:
                print("Please enter a number between 1 and 7.")
                return self.colPos()
            if self.board[0][col] != ' ':
                print("The column is already full! Enter into another column!")
                return self.colPos()
            return col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            return self.colPos()

    def enterToken(self, col, curPlayer):
        for i in range(5, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = curPlayer
                return i
        
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

    def playAgain(self):
        response = input("Do you want to play again? (y/n)\n")
        if response.lower() in {'y', 'yes', 'ok', 'okay', 'k'}:
            self.initBoard()
            self.slotsRemaining = 42
        elif response.lower() in {'n', 'no', 'na', 'nop', 'nope'}:
            print("Red's total wins: " + str(self.redWins))
            print("Yellow's total wins: " + str(self.yellowWins))
            self.slotsRemaining = 0


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
