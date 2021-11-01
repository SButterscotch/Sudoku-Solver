


from os import truncate


board = [
        [5, 3, "x", "x", "x", "x", "x", "x", "x"],
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
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == "x":
                return (row, col)


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

def solve(bo, numTimesRun):
    print("Trying....")
    print_board(bo)
    
    free = is_free(bo)
    if not free:
        print(f"Done! ran {numTimesRun} times")
        return True
    else:
        row, col = free
    
    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo, numTimesRun+1):
                
                return True


            bo[row][col] = "x"
    
    return False

solve(board, 0)

