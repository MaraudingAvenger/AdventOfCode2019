import itertools

BOARD_SIZE = 20
ORIGIN = (BOARD_SIZE // 2, BOARD_SIZE // 2)

grid = []

for y in range(BOARD_SIZE):
    grid.append(list())
    for x in range(BOARD_SIZE):
        grid[y].append(".")


grid[ORIGIN[0]][ORIGIN[1]] = "O"  # starting point

with open("day3sample.txt", "r") as file:
    wireOne = [(item[0], int(item[1:])) for item in file.readline().split(",")]
    wireTwo = [(item[0], int(item[1:])) for item in file.readline().split(",")]


def right(grid, startX, startY, distance, marker="|-+", first=False):
    if not first:
        grid[startY][x] = marker[2]
    for x in range(startX + 1, startX + distance + 1):
        if grid[startY][x] == ".":
            grid[startY][x] = marker[1]
        elif grid[startY][x] in marker:
            grid[startY][x] = marker[2]
        else:
            grid[startY][x] = "M"
    return grid, x, startY


def left(grid, startX, startY, distance, marker="|-+", first=False):
    if not first:
        grid[startY][x] = marker[2]
    for x in range(startX - 1, startX - distance - 1, -1):
        if grid[startY][x] == ".":
            grid[startY][x] = marker[1]
        elif grid[startY][x] in marker:
            grid[startY][x] = marker[2]
        else:
            grid[startY][x] = "M"
    return grid, x, startY


def up(grid, startX, startY, distance, marker="|-+", first=False):
    if not first:
        grid[y][startX] = marker[2]
    for y in range(startY - 1, startY - distance - 1, -1):
        if grid[y][startX] == ".":
            grid[y][startX] = marker[0]
        elif grid[y][startX] in marker:
            grid[y][startX] = marker[2]
        else:
            grid[y][startX] = "M"
    return grid, startX, y


def down(grid, startX, startY, distance, marker="|-+", first=False):
    if not first:
        grid[y][startX] = marker[2]
    for y in range(startY + 1, startY + distance + 1):
        if grid[y][startX] == ".":
            grid[y][startX] = marker[0]
        elif grid[y][startX] in marker:
            grid[y][startX] = marker[2]
        else:
            grid[y][startX] = "M"
    return grid, startX, y


moveDict = {"U": up, "D": down, "L": left, "R": right}

x, y = ORIGIN

wireOneMarker = "|-+"
wireTwoMarker = "\u2551\u2550\u256c"

for d in wireOne:
    try:
        grid, x, y = moveDict[d[0]](grid, x, y, d[1], wireOneMarker)
    except:
        print("current X, Y:", (x, y))
        print(f"trying to move {d[0]}, {d[1]} spaces.")
        break

x, y = ORIGIN

for d in wireTwo:
    try:
        grid, x, y = moveDict[d[0]](grid, x, y, d[1], wireTwoMarker)
    except:
        print("current X, Y:", (x, y))
        print(f"trying to move {d[0]}, {d[1]} spaces.")
        break

for row in grid:
    print("[", end=" ")
    for bip in row:
        print(bip, end=" ")
    print("]")
