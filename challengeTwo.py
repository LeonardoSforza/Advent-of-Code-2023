from collections import defaultdict

file = open('data.txt', 'r')
data = file.read()
data = data.split("\n")

mapOfCards = defaultdict(list)

totalNumberOfScratchCards = 0
cardNum = 1

# First Populate mapOfCards - Takes a few min
for card in data:
    winningNumbers = card.split("|")[0].split(":")[1].strip().split(" ")
    yourNumbers = card.split("|")[1].strip().split(" ")
    mapOfCards[cardNum] = [1, winningNumbers, yourNumbers]
    cardNum += 1

for key, value in mapOfCards.items():
    print(value[0])
    totalNumberOfScratchCards += value[0]
    if value[0] > 0:
        for j in range(1, value[0] + 1):
            cardPoints = 0
            for num in value[2]:
                if num == "":
                    continue
                if num in value[1]:
                    cardPoints += 1
            if cardPoints > 0:
                for i in range(1, cardPoints + 1):
                    newValue = mapOfCards[key+i][0] + 1
                    mapOfCards[key+i] = [newValue, mapOfCards[key+i][1], mapOfCards[key+i][2]]

print(totalNumberOfScratchCards)