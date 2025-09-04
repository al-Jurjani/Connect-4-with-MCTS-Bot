import numpy as np
from Board import Board
from monteCarlo import mcts, Node
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
        bot = mcts()
        while(not self.board.gameFinished):
            self.board.printBoard()
            if (self.board.slotsRemaining % 2 == 0):
                print("Slots remaining: " + str(self.board.slotsRemaining))
                print("Bots turn!")
                curPlayer = self.board.curPlayerBot()
                node = Node(self.board, None, [], 0, 0, False, -1)
                col = mcts().search(node, curPlayer)
                print(col)
                self.board.updateBoard(col, curPlayer)
                row = self.board.height[col]
            else:
                print("Player's turn: ")
                curPlayer = self.board.curPlayer()
                col = Board.colPos(self.board)
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

# test = Board()
# test.board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                       [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                       [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                       [' ', 'X', 'X', 'O', ' ', ' ', ' '],
#                       ['X', 'X', 'O', 'O', ' ', ' ', ' '],
#                       ['X', 'O', 'O', 'O', 'X', ' ', ' ']])
# test.height = np.array([4, 3, 3, 3, 5, 6, 6])
# test.slotsRemaining = 30

# testNode = Node(test, None, [], 0, 0, False, -1)
# col = mcts(testNode).search(testNode, 'X')
# print(col)

if __name__ == "__main__":
    game = connect4()
    game.playGame()
