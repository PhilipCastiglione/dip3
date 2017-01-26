class Cell:
    def __init__(self, idx):
        self.idx = idx
        self.row = idx // 8 + 1
        self.col = idx % 8 + 1
        self.queen = False

class Board:
    def __init__(self):
        self.cells = []

    def visible_cells(self, idx):
        cell = self.cells[idx]
        cells = []
        cells.extend(self.cells_in_dir(cell, self.nw))
        cells.extend(self.cells_in_dir(cell, self.n))
        cells.extend(self.cells_in_dir(cell, self.ne))
        cells.extend(self.cells_in_dir(cell, self.w))
        cells.extend(self.cells_in_dir(cell, self.e))
        cells.extend(self.cells_in_dir(cell, self.sw))
        cells.extend(self.cells_in_dir(cell, self.s))
        cells.extend(self.cells_in_dir(cell, self.se))
        return cells

    def cells_in_dir(self, cell, dir, acc_cells=[]):
        next_cell = dir(cell)
        if next_cell is not None:
            return self.cells_in_dir(next_cell, dir, acc_cells + [next_cell])
        else:
            return acc_cells

    def nw(self, cell):
        if cell.row > 1 and cell.col > 1:
            return self.cells[cell.idx - 9]

    def n(self, cell):
        if cell.row > 1:
            return self.cells[cell.idx - 8]

    def ne(self, cell):
        if cell.row > 1 and cell.col < 8:
            return self.cells[cell.idx - 7]

    def w(self, cell):
        if cell.col > 1:
            return self.cells[cell.idx - 1]

    def e(self, cell):
        if cell.col < 8:
            return self.cells[cell.idx + 1]

    def sw(self, cell):
        if cell.row < 8 and cell.col > 1:
            return self.cells[cell.idx + 7]

    def s(self, cell):
        if cell.row < 8:
            return self.cells[cell.idx + 8]

    def se(self, cell):
        if cell.row < 8 and cell.col < 8:
            return self.cells[cell.idx + 9]

board = Board()
board.cells = [Cell(i) for i in range(64)]

print("cell 35")
for cell in board.visible_cells(35):
    print(cell.idx)

#for cell in board.cells:
    #print("{} {} {}".format(cell.idx, cell.row, cell.col))
    # NB: every queen can attack every other queen we only need to check if the
    # current examined square can attack any queens
    # see if you can attack any queens from the square
    # if so, move on
    # if not, place a queen then move on
