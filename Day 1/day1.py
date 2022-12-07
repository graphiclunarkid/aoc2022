with open('input.txt') as f:
    input = f.readlines()

elves = [i.rstrip() for i in input]

calorie_totals = []
elf_calories = 0

for calories in elves:
    if calories != '':
        elf_calories += int(calories)
    else:
        calorie_totals.append(elf_calories)
        elf_calories = 0

calorie_totals.sort(reverse=True)

print("Part 1:", max(calorie_totals))
print("Part 2:", sum(calorie_totals[:3]))