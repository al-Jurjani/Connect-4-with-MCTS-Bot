import copy
import numpy as np
from Board import Board
import random
import math

EXPLORATION_PARAMETER = math.sqrt(2)

class Node:
    board = Board()
    parent = None
    children = []
    visitCount = 0
    winScore = 0
    expanded = False
    col = -1

    def __init__(self, board, parent, children, visitCount, winScore, expanded, col) -> None:
        self.board = board
        self.parent = parent
        self.children = children
        self.visitCount = visitCount
        self.winScore = winScore
        self.expanded = expanded
        self.col = col

class mcts: 
    def __init__(self, root):
        self.root = root

    def search(self, node = Node, token = str) -> int:
        col = -1
        scoreSheet = {1: 1, 0: -1}
        for i in range(50):
            # print("Root Node")
            # print(node.board.board)

            # Step 1: Selection
            print("SELECTION")
            while node.expanded:
                # print("SOME CHILD SELECTED")
                node = self.selection(node)
                # print("Node Selected: ")
                # print(node.board.board)
            print()

            # Step 2: Expansion
            print("EXPANSION")
            self.expansion(node)
            # print("EXPANSION COMPLETE.")
            # print("CHILDREN GENERATED = " + str(node.children))
            node = random.choice(node.children)
            print()

            # Step 3: Simulation
            print("SIMULATION")
            # print("Node Selected")
            # print(node.board.board)
            print()
            win = self.simulation(node, token)
            # print("Bot win? " + str(win))
            score = scoreSheet.get(win, 0)
            # print("Score for this branch: " + str(score) + "\n")

            # Step 4: Back-Propogation
            print("Back Propogation")
            node = self.backProp(score, node)
            print()

        print("SEARCH COMPLETE")
        for i in node.children:
            print(i.board.board)
            print("Node Visit Count:" + str(i.visitCount))
            print("Node Win Score: " + str(i.winScore))
        col = max(node.children, key=lambda n: n.winScore / n.visitCount).col
        print("Column chosen: " + str(col))
        return col

    def calc_ucb(self, node = Node):
        if node.visitCount == 0: return float('inf')
        return node.winScore / node.visitCount + EXPLORATION_PARAMETER * math.sqrt(math.log(node.parent.visitCount) / node.visitCount)

    # Select node and apply UCB, move to next node
    def selection(self, node = Node):
        if len(node.children) == 0: return None
        return sorted(node.children, key=lambda n: self.calc_ucb(n))[-1]

    # expand nodes until leaf is reached, or time runs out
    def expansion(self, node = Node):
        if node.expanded == False:
            moves = node.board.listOfMoves()
            for i in moves:
                newBoard = copy.deepcopy(node.board)
                newBoard.updateBoard(i, newBoard.curPlayerBot())
                newNode = Node(newBoard, node, [], 0, 0, False, i)
                # print(newNode.board.board)
                node.children.append(newNode)
                node.expanded = True

    # simulate from given node to end node, whether leaf or before
    def simulation(self, node = Node, token = str):
        newBoard = copy.deepcopy(node.board)
        for i in range(0, 7): # Check if current board already has a winning configuration
            row = newBoard.height[i]
            if row != 6:
                if newBoard.checkFour(newBoard.height[i], i, curPlayer='X'):
                    print("Chosen node's board already has a winning configuration")
                    if (token == 'X'): # Game ended with bot win, not a draw
                        print("Bot won!")
                        return 1
                    else:
                        print("Bot lost/Game Drawn")
                        return 0
                elif newBoard.checkFour(newBoard.height[i], i, curPlayer='O'):
                    print("Chosen node's board already has a winning configuration")
                    if (token == 'O'): # Game ended with bot win, not a draw
                        print("Bot won!")
                        return 1
                    else:
                        print("Bot lost/Game Drawn")
                        return 0
        
        while not newBoard.gameFinished:
            move = random.choice(newBoard.listOfMoves())
            tempToken = newBoard.curPlayerBot()
            newBoard.updateBoard(move, tempToken)
            # print("New Board:")
            # print(newBoard.board)
            newBoard.checkFour(newBoard.height[move], move, tempToken)
        # print(newBoard.board)
        if (tempToken == token and newBoard.slotsRemaining != 0): # Game ended with bot win, not a draw
            print("Bot won!")
            return 1
        else:
            print("Bot lost/Game Drawn")
            return 0

    # go back up the path, updating values
    def backProp(self, score, node = Node):
        while node is not None:
            # print("Current node: ")
            # print(node.board.board)
            node.winScore += score
            node.visitCount += 1
            # print("Win Score of node: " + str(node.winScore))
            # print("Visit Count of node:" + str(node.visitCount))
            node = node.parent
            if node.parent is None:
                # print("Parent node: ")
                # print(node.board.board)
                node.winScore += score
                node.visitCount += 1
                # print("Win Score of node: " + str(node.winScore))
                # print("Visit Count of node:" + str(node.visitCount))
                return node


test = Board()
test.board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'X', ' ', ' ', ' ']])
test.height = np.array([6, 6, 6, 4, 6, 6, 6])
test.slotsRemaining = 40

testNode = Node(test, None, [], 0, 0, False, -1)
col = mcts(testNode).search(testNode, 'X')
print(col)