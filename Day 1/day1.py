with open('input.txt') as f:
    input = f.readlines()

list = [i.rstrip() for i in input]

totals = []

sum = 0
for l in list:
    if l != '':
        sum += int(l)
    else:
        totals.append(sum)
        sum = 0

print(max(totals))
