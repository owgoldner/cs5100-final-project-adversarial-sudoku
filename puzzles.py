from board import Board

def getOneAway():
    board = getEasier()
    board.setValue((0,3), 5)
    board.setValue((4,0), 8)
    board.setValue((3,4), 1)
    board.setValue((5,4), 3)
    board.setValue((4,8), 1)
    return board

def getEasier():
    board = getEasy()
    board.setValue((3,0), 6)
    board.setValue((4,1), 9)
    board.setValue((4,3), 6)
    board.setValue((4,7), 2)
    board.setValue((3,6), 8)
    board.setValue((5,6), 6)
    board.setValue((5,8), 4)
    board.setValue((6,0), 9)
    board.setValue((6,3), 1)
    board.setValue((8,7), 1)
    return board

def getEasy():
    board = Board()
    board.setValue((0,2), 8)
    board.setValue((0,7), 4)
    board.setValue((0,8), 6)
    board.setValue((1,0), 4)
    board.setValue((1,1), 6)
    board.setValue((1,3), 3)
    board.setValue((1,4), 8)
    board.setValue((1,5), 9)
    board.setValue((2,0), 5)
    board.setValue((2,1), 1)
    board.setValue((2,3), 4)
    board.setValue((2,4), 6)
    board.setValue((2,6), 2)
    board.setValue((3,3), 7)
    board.setValue((3,5), 2)
    board.setValue((3,8), 3)
    board.setValue((4,2), 3)
    board.setValue((4,4), 5)
    board.setValue((4,6), 7)
    board.setValue((5,0), 1)
    board.setValue((5,3), 9)
    board.setValue((5,5), 8)
    board.setValue((6,2), 4)
    board.setValue((6,4), 7)
    board.setValue((6,5), 6)
    board.setValue((6,7), 8)
    board.setValue((6,8), 2)
    board.setValue((7,3), 2)
    board.setValue((7,4), 9)
    board.setValue((7,5), 5)
    board.setValue((7,7), 6)
    board.setValue((7,8), 7)
    board.setValue((8,0), 2)
    board.setValue((8,1), 7)
    board.setValue((8,6), 5)
    return board


def getEvil():
    game = Board()
    game.setValue((0,3), 8)
    game.setValue((0,8), 9)
    game.setValue((1,5), 4)
    game.setValue((1,6), 6)
    game.setValue((1,7), 2)
    game.setValue((2,1), 5)
    game.setValue((2,7), 8)
    game.setValue((2,8), 1)
    game.setValue((3,2), 4)
    game.setValue((3,4), 8)
    game.setValue((4,1), 9)
    game.setValue((4,3), 5)
    game.setValue((4,4), 2)
    game.setValue((4,5), 1)
    game.setValue((4,7), 3)
    game.setValue((5,4), 9)
    game.setValue((5,6), 2)
    game.setValue((6,0), 5)
    game.setValue((6,1), 3)
    game.setValue((6,7), 4)
    game.setValue((7,1), 2)
    game.setValue((7,2), 7)
    game.setValue((7,3), 6)
    game.setValue((8,0), 1)
    game.setValue((8,5), 9)
    return game