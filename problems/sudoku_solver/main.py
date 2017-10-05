from sudoku import Sudoku
import random

board = [[str(random.randint(1, 9)) for i in range(0, 9)] for j in range(0, 9)]

sudo = Sudoku(board)

print(sudo)