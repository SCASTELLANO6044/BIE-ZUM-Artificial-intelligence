def load_sudoku(file_name):
    f = open(file_name)
    sudoku = f.read()
    f.close()
    return conver_sudoku(sudoku)

def conver_sudoku(board):
    conver_sudoku = []
    lines = board.splitlines()
    for line in lines:
        conver_sudoku.append(list(line))
    #Cast String to int
    aux = []
    for i in range(len(conver_sudoku)):
        aux1 = []
        for j in range(len(conver_sudoku[0])):
            aux1.append(int(conver_sudoku[i][j]))
        aux.append(aux1)
    return aux

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0

    return False

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

board = load_sudoku(".\sudokus\s3.txt")
print_board(board)
solve(board)
print("_______________________")
print("Solution of the sudoku:")
print_board(board)