file = open('data.txt', 'r')
data = file.read()

arrayWords = data.split("\n")

totalSum = 0

for word in arrayWords:
    firstNum = None
    lastNum = None
    for character in word:
        if character.isdigit() and firstNum == None:
            firstNum = character
        if character.isdigit():
            lastNum = character
    totalSum += int(firstNum + lastNum)

print(totalSum)