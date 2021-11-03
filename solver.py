
import os

from os import truncate
with open("tracker.txt", "w") as file:
    file.close()

board = [
        ["x", "x", 5, 3, "x", "x", "x", "x", "x"],
        [8, "x", "x", "x", "x", "x", "x", 2, "x"],
        ["x", 7, "x", "x", 1, "x", 5, "x", "x"],
        [4, "x", "x", "x", "x", 5, 3, "x", "x"],
        ["x", 1, "x", "x", 7, "x", "x", "x", 6],
        ["x", "x", 3, 2, "x", "x", "x", 8, "x"],
        ["x", 6, "x", 5, "x", "x", "x", "x", 9],
        ["x", "x", 4, "x", "x", "x", "x", 3, "x"],
        ["x", "x", "x", "x", "x", 9, 7, "x", "x"]

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

def tracker():
    with open("tracker.txt", "a") as file:
        file.write("x")

def counter():
    with open("tracker.txt", "r") as file:
        str = file.read()
        count = len(str)
        return count

def solve(bo):
    
    print(f"Trying {counter()} times!")
    print_board(bo)
    
    
    
    free = is_free(bo)
    if not free:
        print("\n-------------------------------------------------\n")
        print_board(bo)
        print(f"Done! ran {counter()} times")
        
        os.remove("tracker.txt")
        return True
    else:
        row, col = free
    
    for i in range(1, 10):
        tracker()
        
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                
                return True


            bo[row][col] = "x"
    
    return False



solve(board)

