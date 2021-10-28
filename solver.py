


from os import truncate


board = [
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"]

]


def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end= "")
            
            if j == 8:
                print(bo[i][j])

            else:
                print(f"{bo[i][j]} ", end="")


def is_free(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == "x":
                return (i, j)


def is_valid(bo, num, pos):
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False
    
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(bo):
    free = is_free(bo)
    if not free:
        return True
    else:
        row, col = free

    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True


            bo[row][col] = "x"
    
    return False
print_board(board)
solve(board)
print("________________________________\n")
print_board(board)