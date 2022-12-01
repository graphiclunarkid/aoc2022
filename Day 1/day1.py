with open('input.txt') as f:
    input = f.readlines()

list = [i.rstrip() for i in input]

totals = []
elf_calories = 0

for l in list:
    if l != '':
        elf_calories += int(l)
    else:
        totals.append(elf_calories)
        elf_calories = 0

totals.sort(reverse=True)

print("Part 1:", max(totals))
print("Part 2:", sum(totals[:3]))