import math


def calc_fuel_recursive(x):
    calc = math.floor(x / 3) - 2
    if calc > 0:
        return calc + calc_fuel_recursive(calc)
    return 0


def calc_fuel(x):
    return math.floor(x / 3) - 2


if __name__ == "__main__":
    with open("day1-1.txt", "r") as f:
        total_fuel = sum(
            [calc_fuel_recursive(int(line.strip())) for line in f.readlines()]
        )
    print(total_fuel)
