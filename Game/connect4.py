import numpy as np
from Board import Board
class connect4:
    redWins = 0
    yellowWins = 0
    board = Board()
 
    def __init__(self) -> None:
        pass

    def playGame(self):
        col = -1
        row = -1
        curPlayer = ' '
        while(self.board.slotsRemaining > 0):
            self.board.printBoard()
            curPlayer = self.curPlayer(self.board.slotsRemaining)
            col = self.colPos(self.board)
            self.board.updateBoard(col, curPlayer)
            row = self.board.height[col]

            if self.board.checkFour(row, col, curPlayer):
                self.board.printBoard()
                print("Player '" + curPlayer + "' has won!")
                if curPlayer == 'X':
                    self.redWins += 1
                else:
                    self.yellowWins += 1
                self.playAgain()
            elif (self.board.slotsRemaining == 0):
                print("All slots filled! Game drawn!")
                self.playAgain()

    def curPlayer(self, slotsRemaining):
        if slotsRemaining % 2 == 0:
            print("Player 1's turn. Token = 'X'")
            return 'X'
        else:
            print("Player 2's turn. Token = 'O'")
            return 'O'

    def colPos(self, board):
        try:
            col = int(input("Choose what column to insert your token in: 1-7\n")) - 1
            if col < 0 or col > 6:
                print("Please enter a number between 1 and 7.")
                return self.colPos(board)
            if board.height[col] == 0:
                print("The column is already full! Enter into another column!")
                return self.colPos(board)
            return col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            return self.colPos(board)

    def playAgain(self):
        response = input("Do you want to play again? (y/n)\n")
        if response.lower() in {'y', 'yes', 'ok', 'okay', 'k'}:
            self.board.initBoard()
            return 42, np.array([6, 6, 6, 6, 6, 6, 6])
        elif response.lower() in {'n', 'no', 'na', 'nop', 'nope'}:
            print("Red's total wins: " + str(self.redWins))
            print("Yellow's total wins: " + str(self.yellowWins))
            self.board.slotsRemaining = 0

game = connect4()
game.playGame()
