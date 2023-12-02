file = open('data.txt', 'r')
data = file.read()

arrayGames = data.split("\n")

maxRed = 12
maxGreen = 13
maxBlue = 14

sumPossibleGames = 0

for game in arrayGames:
    isThisGameImpossible = False
    i = 6
    while game[i] != ':':
        i += 1
    gameNum = game[5:i]
    # print(gameNum)
    revelas = game[i+2:].split(";")

    for reveal in revelas:
        reveal = reveal.split(",")
        for singleValue in reveal:
            num = singleValue.strip().split(" ")[0]
            color = singleValue.strip().split(" ")[1]

            if color == "red" and int(num) > maxRed:
                isThisGameImpossible = True
            if color == "blue" and int(num) > maxBlue:
                isThisGameImpossible = True
            if color == "green" and int(num) > maxGreen:
                isThisGameImpossible = True
    
    if not isThisGameImpossible:
        sumPossibleGames += int(gameNum)

print(sumPossibleGames)
