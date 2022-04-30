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

        while len(queue) != 0:
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

        # self.board.printBoard()
        return 

