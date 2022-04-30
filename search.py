from cmath import inf
from random import choice
from adversarial import Game

from solver import Solver


class Minimax:

    def minimax(self, game, player, d = 10):
        self.DEPTH = d
        actions = self.getActions(game)
        if len(actions.keys()) == 0:
            print("no move")
            return

        maxVal = -inf
        maxAction = None

        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v = self.minValue(result, player, 1, -inf, inf)
            if maxAction is None or v > maxVal:
                maxVal = v
                maxAction = (a, actions[a])
        
        print("Recommended move: " + str(maxAction[1]) + " at row " + str(maxAction[0][0] + 1) + ", column " + str(maxAction[0][1] + 1))
        print("Projected score: " + str(maxVal))
        return maxAction


    def maxValue(self, game, player, iteration, alpha, beta):
        if game.board.isBoardFull() or iteration >= self.DEPTH:
            return game.score[player]
        v = -inf
        actions = self.getActions(game)
        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v = max(v, self.minValue(result, player, iteration + 1, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
        
    def minValue(self, game, player, iteration, alpha, beta):
        if game.board.isBoardFull() or iteration >= self.DEPTH:
            return game.score[player]
        v = inf
        actions = self.getActions(game)
        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v = min(v, self.maxValue(result, player, iteration + 1, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def getActions(self, game):
        actions = {}
        solved = game.board.copy()
        solver = Solver(solved)
        solver.solve()
        if not solved.isBoardFull():
            print("Board has no valid solutions")
            return actions
        for i in range(9):
            for j in range(9):
                if not game.board.hasValue((i,j)):
                    actions[(i,j)] = solved.getValue((i,j))
        return actions

class Expectimax(Minimax):

    def expectimax(self, game, player, d = 10):
        self.DEPTH = d
        actions = self.getActions(game)
        if len(actions.keys()) == 0:
            print("no move")
            return

        maxVal = -inf
        maxAction = None

        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v = self.expectedValue(result, player, 1)
            if maxAction is None or v > maxVal:
                maxVal = v
                maxAction = (a, actions[a])
        
        print("Recommended move: " + str(maxAction[1]) + " at row " + str(maxAction[0][0] + 1) + ", column " + str(maxAction[0][1] + 1))
        print("Projected score: " + str(maxVal))
        return maxAction

    def maxValue(self, game, player, iteration):
        if game.board.isBoardFull() or iteration >= self.DEPTH:
            return game.score[player]
        v = -inf
        actions = self.getActions(game)
        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v = max(v, self.expectedValue(result, player, iteration + 1))
        return v

    def expectedValue(self, game, player, iteration):
        if game.board.isBoardFull() or iteration >= self.DEPTH:
            return game.score[player]
        v = 0
        actions = self.getActions(game)
        count = 0
        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v += self.maxValue(result, player, iteration + 1)
            count += 1
        return v / count


class Randimax(Minimax):

    def randimax(self, game, player, d = 10):
        self.DEPTH = d
        actions = self.getActions(game)
        if len(actions.keys()) == 0:
            print("no move")
            return

        maxVal = -inf
        maxAction = None

        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v = self.expectedValue(result, player, 1)
            if maxAction is None or v > maxVal:
                maxVal = v
                maxAction = (a, actions[a])
        
        print("Recommended move: " + str(maxAction[1]) + " at row " + str(maxAction[0][0] + 1) + ", column " + str(maxAction[0][1] + 1))
        print("Projected score: " + str(maxVal))
        return maxAction

    def maxValue(self, game, player, iteration):
        if game.board.isBoardFull() or iteration >= self.DEPTH:
            return game.score[player]
        v = -inf
        actions = self.getActions(game)
        for a in actions.keys():
            result = Game(game.board.copy())
            result.turn = game.turn
            result.score[0] = game.score[0]
            result.score[1] = game.score[1]
            result.playMove(a, actions[a])
            v = max(v, self.expectedValue(result, player, iteration + 1))
        return v

    def expectedValue(self, game, player, iteration):
        if game.board.isBoardFull() or iteration >= self.DEPTH:
            return game.score[player]
        v = inf
        actions = self.getActions(game)
        a = choice(list(actions.keys()))
        result = Game(game.board.copy())
        result.turn = game.turn
        result.score[0] = game.score[0]
        result.score[1] = game.score[1]
        result.playMove(a, actions[a])
        v = min(v, self.maxValue(result, player, iteration + 1))
        return v