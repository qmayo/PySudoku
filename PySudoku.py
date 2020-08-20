class Sudoku:
    def __init__(self, board, cells):
        self.board = board
        self.cells = cells

    #Creates a board
    def newboard(self):
        values = self.cells.split(" ")
        val_counter = 0

        if len(values) != 81:
            print("Error: Not 81 values.")
            exit()

        else:
            for i in range(9):
                for j in range(9):
                    self.board[i][j] = int(values[val_counter])
                    val_counter += 1

    # Returns new cell pos
    def findValidCell(self):
        for i in range(9):
            for j in range(9):
                if int(self.board[i][j]) == 0:
                    return i, j
        return -1


    def possible(self, row, col, val):
        # Check row for value
        for i in range(9):
            if self.board[row][i] == val:
                return False
        # Checks col for value
        for j in range(9):
            if self.board[j][col] == val:
                return False
        # Checks square for value
        coordX, coordY = 3 * (row // 3), 3 * (col // 3)
        for x in range(coordX, coordX + 3):
            for y in range(coordY, coordY + 3):
                if x == row and y == col:
                    continue
                if self.board[x][y] == val:
                    return False
        return True



        # Solves the board

    def solve(self):
        # Checks if cells are all solved
        if self.findValidCell() == -1:
            print(self.board)
            return True

        # Finds first cell to fill
        row, col = self.findValidCell()

        for i in range(1, 10):
            if self.possible(row, col, i):
                self.board[row][col] = i
                # Updates values to find new cell to fill

                if self.solve():
                    return True
                # Backtracks
                self.board[row][col] = 0

        return False


# Get cell values and calls solve function
get_cells = input("Enter cell values seperated by 1 space. Enter 0 for empty cells: ")
b = Sudoku([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]], get_cells)
b.newboard()
b.solve()

