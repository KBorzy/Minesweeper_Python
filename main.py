import random

# Minesweeper game simulator.
# In each empty field there is a number that indicates how much bombs are around this field (vertically, horizontally or diagonally).
# It's program that after loading the board containing only information about bombs will prepare a ready game board Minesweeper.
# A bomb is marked with "*" and an empty field with "." As output, the program print a ready Minesweeper game board


# auxiliary variable
MINE = 1
EMPTY = 0
UNKNOWN = 0

# size of board
w, h = 5, 3
grid = [[0 for x in range(w)] for y in range(h)]


# generate and put on board 3 bombs
for bomb in range(3):
    r = random.randint(0, 2)
    c = random.randint(0, 4)
    grid[r][c] = '*'


# print grid in terminal
def show_grid():
    symbols = {0: 0}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            value = grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"{symbol} ", end='')
        print("")

# counting mines around the field
def count(row, col):
    offsets = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    count = 0
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]

        # check if bomb, if yes add +1 to value of field
        if ((offset_row >= 0 and offset_row <= 2) and (offset_col >= 0 and offset_col <= 4)):
            if grid[offset_row][offset_col] == ('*'):
                count += 1
    return count

# check the field is empty or has a mine
def check():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ['*']:
                continue
            elif grid[row][col] == UNKNOWN:
                grid[row][col] = count(row, col)

                # find all cells and their values
                cells = [(row, col)]
                offsets = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

                while len(cells) > 0:
                    cell = cells.pop()
                    for offset in offsets:
                        row = offset[0] + cell[0]
                        col = offset[1] + cell[1]
                        if ((row >= 0 and row <= 2) and (col >= 0 and col <= 4)):
                            if (grid[row][col] == ('.')):
                                grid[row][col] = count(row, col)

                                if count(row, col) == EMPTY and (row, col) not in cells:
                                    cells.append((row, col))
                                else:
                                    grid[row][col] = count(row, col)



check()
show_grid()
