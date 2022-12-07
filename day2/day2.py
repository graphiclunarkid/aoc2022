with open('input.txt') as f:
    input = f.readlines()

games = [i.rstrip() for i in input]

print(games)