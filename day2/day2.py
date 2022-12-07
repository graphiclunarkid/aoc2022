with open('input.txt') as f:
    input = f.readlines()

cleanedInput = [i.rstrip() for i in input]
games = [tuple(map(str, sub.split(' '))) for sub in cleanedInput]

winConditions  = [("A", "Y"), ("B", "Z"), ("C", "X")]
drawConditions = [("A", "X"), ("B", "Y"), ("C", "Z")]
loseConditions = [("A", "Z"), ("B", "X"), ("C", "Y")]

score = 0

rock = 1
paper = 2
scissors = 3
lose = 0
draw = 3
win = 6

def getShapeScore(shape):
    if shape == "X":
        return rock
    elif shape == "Y":
        return paper
    elif shape == "Z":
        return scissors
    else:
        raise Exception("Input error")

def getOutcomeScore(game):
    if game in winConditions:
        return win
    elif game in drawConditions:
        return draw
    elif game in loseConditions:
        return lose
    else:
        raise Exception("Input error")

def getScore(game):
    if game[0] == "A":
        if game[1] == "X":
            return scissors + lose
        elif game[1] == "Y":
            return rock + draw
        elif game[1] == "Z":
            return paper + win
        else:
            raise Exception("Input error")

    elif game[0] == "B":
        if game[1] == "X":
            return rock + lose
        elif game[1] == "Y":
            return paper + draw
        elif game[1] == "Z":
            return scissors + win
        else:
            raise Exception("Input error")
            
    elif game[0] == "C":
        if game[1] == "X":
            return paper + lose
        elif game[1] == "Y":
            return scissors + draw
        elif game[1] == "Z":
            return rock + win
        else:
            raise Exception("Input error")
            
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