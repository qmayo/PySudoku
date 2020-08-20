#This program solves sudoku puzzles
import copy
import sys

class Sudoku:
    def __init__(self, board, cells):
        self.board = board
        self.cells = cells

    #Creates a board
    def newboard(self):
        values = self.cells.split(" ")
        val_counter = 0
        if len(values) != 81:
            raise Exception("Error: You entered less than 81 cell values.")
        else:
            for i in range(9):
                for j in range(9):
                    self.board[i][j] = values[val_counter]
                    val_counter += 1

    #Returns row
    def findValidRow(self):
        for i in range(9):
            for j in range(9):
                if int(self.board[i][j]) == 0:
                    return i
        return False
   #Returns col
    def findValidCol(self):
        for i in range(9):
            for j in range(9):
                if int(self.board[i][j]) == 0:
                    return j
        return False

    def possible(self, row, col, val):
        #Check row for value
        for i in range(9):
            if self.board[row][i] == val:
                return False
        #Checks col for value
        for j in range(9):
            if self.board[j][col]:
                return False
        #Checks square for value
        if col in [1,4,7]:
            



                    

    #Solves the board
    def solve(self):
        if self.findValidCol == False:
            return True
        row = copy.deepcopy(self.findValidRow)
        col = copy.deepcopy(self.findValidCol)
        for i in range(1,10):
            if self.possible(row, col, i) == True:
                self.board[row][col] = i
                row = copy.deepcopy(self.findValidRow)
                col = copy.deepcopy(self.findValidCol)
                if self.solve():
                    return True.
                self.board[row][col] = 0
        return False
        

#Get cell values and call solve function
#Next version will allow uploading of txt files
get_cells = input("Enter cell values seperated by 1 space. Enter 0 for empty cells: ")
b = Sudoku([[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]], get_cells)
b.solve()

