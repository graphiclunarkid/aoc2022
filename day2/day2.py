with open('input.txt') as f:
    input = f.readlines()

cleanedInput = [i.rstrip() for i in input]

games = [tuple(map(str, sub.split(' '))) for sub in cleanedInput]

print (games)