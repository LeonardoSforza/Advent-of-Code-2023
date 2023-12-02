file = open('data.txt', 'r')
data = file.read()

arrayGames = data.split("\n")

maxRed = 12
maxGreen = 13
maxBlue = 14

powerGames = []

for game in arrayGames:
    minRed = 0
    minGreen = 0
    minBlue = 0
    
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

            if color == "red":
                if int(num) > minRed:
                    minRed = int(num) 
            if color == "blue":
                if int(num) > minBlue:
                    minBlue = int(num)
            if color == "green":
                if int(num) > minGreen:
                    minGreen = int(num)

    powerGames.append(minRed * minGreen * minBlue)

totalPower = 0
for power in powerGames:
    totalPower += power

print(totalPower)