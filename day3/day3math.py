with open("day3.txt", "r") as file:
    wireOne = [(item[0], int(item[1:])) for item in file.readline().split(",")]
    wireTwo = [(item[0], int(item[1:])) for item in file.readline().split(",")]


def up(distance, x, y):
    points = [(x, y + i) for i in range(distance + 1)]
    newX, newY = points[-1]
    return newX, newY, points


def down(distance, x, y):
    points = [(x, y - i) for i in range(distance + 1)]
    newX, newY = points[-1]
    return newX, newY, points


def left(distance, x, y):
    points = [(x - i, y) for i in range(distance + 1)]
    newX, newY = points[-1]
    return newX, newY, points


def right(distance, x, y):
    points = [(x + i, y) for i in range(distance + 1)]
    newX, newY = points[-1]
    return newX, newY, points


moveDict = {"U": up, "D": down, "L": left, "R": right}

wireOnePoints = set()
wireTwoPoints = set()
x, y = (0, 0)

for direction in wireOne:
    x, y, points = moveDict[direction[0]](direction[1], x, y)
    for point in points:
        wireOnePoints.add(point)
x, y = (0, 0)

for direction in wireTwo:
    x, y, points = moveDict[direction[0]](direction[1], x, y)
    for point in points:
        wireTwoPoints.add(point)

crosses = {point for point in wireOnePoints if point in wireTwoPoints}
crosses.remove((0, 0))

part1 = min(crosses, key=lambda x: abs(x[0]) + abs(x[1]))
print(f"Part 1 - @point {part1}, with distance {abs(part1[0])+abs(part1[1])}")

crossSteps = []
for cross in crosses:
    steps = 0
    x, y = (0, 0)
    for direction in wireOne:
        x, y, points = moveDict[direction[0]](direction[1], x, y)
        if cross in points:
            for point in points:
                if point == cross:
                    # print(f"wireOne steps: {steps}")
                    break
                steps += 1
            break
        else:
            steps += direction[1]
    x, y = (0, 0)
    for direction in wireTwo:
        x, y, points = moveDict[direction[0]](direction[1], x, y)
        if cross in points:
            for point in points:
                if point == cross:
                    # print(f"+wireTwo steps {steps}")
                    crossSteps.append((cross, steps))
                    break
                steps += 1
            break
        else:
            steps += direction[1]

# print(sorted(crossSteps, key=lambda x: x[1]))
part2 = min(crossSteps, key=lambda x: x[1])
print(f"Part 2 - @point {part2[0]}, with step distance {part2[1]}")
