# Challenge details: https://adventofcode.com/2022/day/1

with open('input.txt') as f:
    input = f.readlines()

list = [i.rstrip() for i in input]

calorie_totals = []
elf_calories = 0

def store(elf_calories):
    calorie_totals.append(elf_calories)
    elf_calories = 0

[ elf_calories += int(calories) if calories != '' else store(elf_calories) for calories in list ]

calorie_totals.sort(reverse=True)

print("Part 1:", max(calorie_totals))
print("Part 2:", sum(calorie_totals[:3]))