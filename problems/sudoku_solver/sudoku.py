""" File containing the Sudoku class """

class Sudoku(object):
    """ Sudoku class"""

    def __init__(self, board):
        self.board = board

    def solve_board(self):
        """ This function will solve the board for a valid sudoku """

    def __str__(self):
        board_str = ''
        for col in self.board:
            board_str += ''.join(col) + '\n'
        return board_str

    def __repr__(self):
        return self.__str__()
