import math


class Game:
    def __init__(self, board):
        self.board = board
        self.turn = 0
        self.score = [0, 0]
        self.rowsCompleted, self.colsCompleted, self.boxesCompleted = [], [], []
        self.checkCompleted()

    def playMove(self, pos, val):
        curr = self.turn % 2
        if self.board.setIfLegal(pos,val):
            self.score[curr] += self.checkCompleted()
        else:
            self.score[curr] -= 1
        self.turn += 1

    def gameOver(self):
        print("Game complete. Final board:")
        self.board.printBoard()
        print("Scores... Player 1: " + str(self.score[0]) + "... Player 2: " + str(self.score[1]))

    def checkCompleted(self):
        inc = 0
        for i in range(9):
            if not i in self.rowsCompleted:
                full = True
                for j in range(9):
                    full = full and self.board.hasValue((i,j))
                if full:
                    self.score[self.turn % 2] += 1
                    self.rowsCompleted.append(i)
                    inc += 1
            if not i in self.colsCompleted:
                full = True
                for j in range(9):
                    full = full and self.board.hasValue((j,i))
                if full:
                    self.score[self.turn % 2] += 1
                    self.colsCompleted.append(i)
                    inc += 1
            if not i in self.boxesCompleted:
                if len(self.board.getBox((math.floor(i / 3) * 3, (i % 3) * 3))) == 9:
                    self.score[self.turn % 2] += 1
                    self.boxesCompleted.append(i)
                    inc += 1
        return inc

    