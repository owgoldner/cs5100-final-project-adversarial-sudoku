from adversarial import Game
from search import Expectimax, Minimax, Randimax
import puzzles
from solver import Solver

game = puzzles.getOneAway()

def playSinglePlayer():
    while not game.isBoardFull():
        print()
        game.printBoard()
        print()
        print("Type q to stop or any other key to continue: ")
        if input() == "q":
            break

        print("Enter a move ----")
        print("Row (1 to 9): ")
        row = int(input()) - 1
        print("Column (1 to 9): ")
        col = int(input()) - 1
        print("Value (1 to 9): ")
        val = int(input())

        result = game.setIfLegal((row, col), val)
        if not result:
            print("Invalid move")

    print("Thank you for playing.")

def playAdversarial():
    adv = Game(game)
    while not game.isBoardFull():
        print()
        game.printBoard()
        print("P1 score: " + str(adv.score[0]) + "... P2 score: " + str(adv.score[1]))
        print()
        print("Type q to stop or any other key to continue: ")
        if input() == "q":
            break
        
        print("P1 move" if adv.turn % 2 == 0 else "P2 move")
        print("Enter a move ----")
        print("Row (1 to 9): ")
        row = int(input()) - 1
        print("Column (1 to 9): ")
        col = int(input()) - 1
        print("Value (1 to 9): ")
        val = int(input())

        adv.playMove((row, col), val)

    print("Thank you for playing.")

def runSolver():
    solver = Solver(game)
    solver.solve()
    game.printBoard()

def runMinimax(adv, depth):
    mm = Minimax()
    player = adv.turn % 2
    action = mm.minimax(adv, player, depth)
    # adv.playMove(action[0], action[1])

def runExpectimax(adv, depth):
    em = Expectimax()
    player = adv.turn % 2
    action = em.expectimax(adv, player, depth)
    # adv.playMove(action[0], action[1])

def runRandimax(adv, depth):
    rm = Randimax()
    player = adv.turn % 2
    action = rm.randimax(adv, player, depth)
    return action
    # adv.playMove(action[0], action[1])

def playMinimax(adv, depth):
    while not adv.board.isBoardFull():
        runMinimax(adv, depth)
        adv.board.printBoard()
    adv.gameOver()

def playExpectimax(adv, depth):
    while not adv.board.isBoardFull():
        runExpectimax(adv, depth)
        adv.board.printBoard()
    adv.gameOver()


def randimaxDistribution(adv, depth, iterations):
    counter = {}
    for _ in range(iterations):
        a = runRandimax(adv, depth)
        if a in counter:
            counter[a] += 1
        else:
            counter[a] = 1
    return counter
