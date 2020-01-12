PUZZ_INPUT = "138307-654504"

low, high = tuple(int(x) for x in PUZZ_INPUT.split("-"))

partOneCount = 0

for potential in range(low, high + 1):
    digits = [int(s) for s in str(potential)]
    if int("".join([str(d) for d in sorted(digits)])) != potential:
        continue
    if not any(digits.count(digit) - 1 for digit in digits):
        continue
    partOneCount += 1

print(f"Part 1 - potential pwds: {partOneCount}")

partTwoCount = 0
for potential in range(low, high + 1):
    digits = [int(s) for s in str(potential)]
    if int("".join([str(d) for d in sorted(digits)])) != potential:
        continue
    if not any(digits.count(digit) - 1 for digit in digits):
        continue
    elif not any(digits.count(digit) == 2 for digit in digits):
        continue
    partTwoCount += 1

print(f"Part 2 - potential pwds: {partTwoCount}")
