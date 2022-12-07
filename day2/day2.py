with open('input.txt') as f:
    input = f.readlines()

cleanedInput = [i.rstrip() for i in input]
games = [tuple(map(str, sub.split(' '))) for sub in cleanedInput]

winConditions  = [("A", "Y"), ("B", "Z"), ("C", "X")]
drawConditions = [("A", "X"), ("B", "Y"), ("C", "Z")]
loseConditions = [("A", "Z"), ("B", "X"), ("C", "Y")]
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
    elif game in loseConditions:
        return 0
    else:
        raise Exception("Input error")

rock = 1
paper = 2
scissors = 3
lose = 0
draw = 3
win = 6

def getScore(game):
    if game[0] == "A":
        if game[1] == "X":
            return scissors + lose
        elif game[1] == "Y":
            return rock + draw
        elif game[1] == "Z":
            return paper + win

    elif game[0] == "B":
        if game[1] == "X":
            return rock + lose
        elif game[1] == "Y":
            return paper + draw
        elif game[1] == "Z":
            return scissors + win

    elif game[0] == "C":
        if game[1] == "X":
            return paper + lose
        elif game[1] == "Y":
            return scissors + draw
        elif game[1] == "Z":
            return rock + win

    else:
        raise Exception("Input error")

for game in games:
    score += getShapeScore(game[1])
    score += getOutcomeScore(game)

print("Part 1: ", score)

score = 0

for game in games:
    score += getScore(game)

print("Part 2: ", score)