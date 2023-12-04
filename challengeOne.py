file = open('data.txt', 'r')
data = file.read()
data = data.split("\n")

returnValue = 0

for card in data:
    winningNumbers = card.split("|")[0].split(":")[1].split(" ")
    yourNumbers = card.split("|")[1].split(" ")
    cardPoints = 0
    for num in yourNumbers:
        if num == "":
            continue
        if num in winningNumbers:
            cardPoints += 1
    
    totalPoints = 0
    if cardPoints > 0:
        for i in range(1, cardPoints + 1):
            if i == 1:
                totalPoints += 1
            else:
                totalPoints *= 2
    returnValue += totalPoints

print(returnValue)