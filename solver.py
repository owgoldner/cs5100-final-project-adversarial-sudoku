from board import Board

class Solver:
    def __init__(self, board):
        self.board = board

    # Returns a valid solution to this object's board if any exists, otherwise returning false
    def solve(self):

        queue = []

        moves = []

        vals = {}

        for i in range(9):
            for j in range(9):
                if not self.board.hasValue((i,j)):
                    queue.insert(0, (i,j))
                    vals[(i,j)] = 1

        iterations = 0
        while len(queue) != 0: # failsafe iteration count in case something breaks
            iterations += 1
            move = queue.pop()
            if not self.board.setIfLegal(move, vals[move]):
                if vals[move] < 9:
                    # try next value
                    vals[move] += 1
                    queue.append(move)
                else:
                    # no values left, try backtracking
                    if len(moves) == 0:
                        print("no valid solution")
                        return
                    else:
                        priorMove = moves.pop()
                        vals[priorMove] += 1
                        vals[move] = 1
                        self.board.removeValue(priorMove)
                        queue.append(move)
                        queue.append(priorMove)
            else:
                moves.append(move)

        self.board.printBoard()
        return 

board = Board()
# board.setValue((0,3), 8)
# board.setValue((0,8), 9)
# board.setValue((1,5), 4)
# board.setValue((1,6), 6)
# board.setValue((1,7), 2)
# board.setValue((2,1), 5)
# board.setValue((2,7), 8)
# board.setValue((2,8), 1)
# board.setValue((3,2), 4)
# board.setValue((3,4), 8)
# board.setValue((4,1), 9)
# board.setValue((4,3), 5)
# board.setValue((4,4), 2)
# board.setValue((4,5), 1)
# board.setValue((4,7), 3)
# board.setValue((5,4), 9)
# board.setValue((5,6), 2)
# board.setValue((6,0), 5)
# board.setValue((6,1), 3)
# board.setValue((6,7), 4)
# board.setValue((7,1), 2)
# board.setValue((7,2), 7)
# board.setValue((7,3), 6)
# board.setValue((8,0), 1)
# board.setValue((8,5), 9)
solver = Solver(board)
solver.solve()