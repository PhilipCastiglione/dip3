class Cell:
    def __init__(self, idx):
        self.idx = idx
        self.row = idx // 8 + 1
        self.col = idx % 8 + 1
        self.queen = False

    def nw_cell_idx(self):
        if self.row > 1 and self.col > 1:
            return idx - 9

    def n_cell_idx(self):
        if self.row > 1:
            return idx - 8

    def ne_cell_idx(self):
        if self.row > 1 and self.col < 8:
            return idx - 7

    def w_cell_idx(self):
        if self.col > 1:
            return idx - 1

    def e_cell_idx(self):
        if self.col < 8:
            return idx + 1

    def sw_cell_idx(self):
        if self.row < 8 and self.col > 1:
            return idx + 7

    def s_cell_idx(self):
        if self.row < 8:
            return idx + 8

    def se_cell_idx(self):
        if self.row < 8 and self.col < 8:
            return idx + 9

class Board:
    def __init__(self):
        self.cells = []
        
    def visible_cells(cell):
        c = self.cells(cell)
        c.nw_cell_idx()


board = Board()
board.cells = [Cell(i) for i in range(64)]

for cell in board.cells:
    print("{} {} {}".format(cell.idx, cell.row, cell.col))
    # NB: every queen can attack every other queen we only need to check if the
    # current examined square can attack any queens
    # see if you can attack any queens from the square
    # if so, move on
    # if not, place a queen then move on
