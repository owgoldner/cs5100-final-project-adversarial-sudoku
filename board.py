import math

# Represents a traditional 9x9 Sudoku board
class Board:
    # Creates an empty 9x9 board with all values initialized to None
    def __init__(self):
        self.array = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(None)
            self.array.append(row)

    # Given position (x, y), sets board position board[x][y] to the given value
    def setValue(self, pos, val):
        self.array[pos[0]][pos[1]] = val

    # Resets the value at the given position to None
    def removeValue(self, pos):
        self.array[pos[0]][pos[1]] = None

    # Returns the value at the given board position
    def getValue(self, pos):
        return self.array[pos[0]][pos[1]]

    # Returns true if a numeric value has been assigned to the given position, false
    # if it is still empty (None)
    def hasValue(self, pos):
        return not (self.array[pos[0]][pos[1]] is None)

    # If the given position is empty, sets to the given value and returns true
    # Else, returns false and does not change the value
    def setIfEmpty(self, pos, val):
        if self.hasValue(pos):
            return False
        
        self.setValue(pos, val)
        return True

    # Performs allDiff checks for the row, column, and box for the given position and proposed value
    def isValidMove(self, pos, val):
        row = pos[0]
        col = pos[1]
        for i in range(9):
            val2 = self.getValue((i, col))
            if not val2 is None and val2 == val:
                return False
            val3 = self.getValue((row, i))
            if not val3 is None and val3 == val:
                return False
        box = self.getBox(pos)
        for n in box:
            if val == n:
                return False
        
        return True

    # Returns a list of all non-None values inside the box that contains the given position
    def getBox(self, pos):
        initRow = math.floor(pos[0] / 3) * 3
        initCol = math.floor(pos[1] / 3) * 3
        vals = []
        for i in range(3):
            for j in range(3):
                val = self.array[initRow + i][initCol + j]
                if not val is None:
                    vals.append(val)

        return vals

    # Sets the given position to the given value if the move is legal according to game rules
    # i.e., there is not already a value in that position and the value is different from all
    # other values in the same row, column, and 3x3 box, and the val is between 1 and 9, incl.
    def setIfLegal(self, pos, val):
        if val in range(1,10) and self.isValidMove(pos, val):
            return self.setIfEmpty(pos, val)

        return False

    # Are all values not None? Does not care if values are valid according to Sudoku rules.
    def isBoardFull(self):
        for i in range(9):
            for j in range(9):
                if not self.hasValue((i, j)):
                    return False

        return True

    # Prints the board to console
    def printBoard(self):
        for i in range(9):
            row = " "
            for j in range(9):
                row += ("_" if self.array[i][j] is None else str(self.array[i][j])) + " "
                if j % 3 == 2 and j != 8:
                    row += "| "
            print(row)
            if i % 3 == 2 and i != 8:
                dashes = ""
                for x in range(23):
                    dashes += "-"
                print(dashes)
                
