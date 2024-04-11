import array as arr
import numpy as np
class connect4:


    redWins = 0
    yellowWins = 0
    playAgain = 'y'
    board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']])
    
    def __init__(self) -> None:
        pass

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
game.printBoard()