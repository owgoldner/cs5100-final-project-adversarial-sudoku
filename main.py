import board

game = board.Board()

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