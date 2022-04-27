class Game:
    def __init__(self, board):
        self.board = board
        self.turn = 0
        self.score = { "p1" : 0, "p2": 0 }
        self.rowsCompleted, self.colsCompleted, self.boxesCompleted = [], [], []

    def getBoard(self):
        return self.board

    