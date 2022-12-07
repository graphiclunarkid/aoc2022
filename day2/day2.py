with open('input.txt') as f:
    input = f.readlines()

cleanedInput = [i.rstrip() for i in input]
games = [tuple(map(str, sub.split(' '))) for sub in cleanedInput]

winConditions = [("A", "Y"), ("B", "Z"), ("C", "X")]
drawConditions = [("A", "X"), ("B", "Y"), ("C", "Z")]
score = 0

def getShapeScore(shape):
    if shape == "X":
        return 1
    elif shape == "Y":
        return 2
    elif shape == "Z":
        return 3
    else:
        raise Exception("Input error")

def getOutcomeScore(game):
    if game in winConditions:
        return 6
    elif game in drawConditions:
        return 3
    else:
        return 0

for game in games:
    score += getShapeScore(game[1])
    score += getOutcomeScore(game)

print("Part 1: ", score)