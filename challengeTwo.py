file = open('data.txt', 'r')
data = file.read()

arrayWords = data.split("\n")

totalSum = 0

listOfNumbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
}

for word in arrayWords:
    firstNum = None
    lastNum = None
    for i in range(0, len(word)):
        if word[i].isdigit() and firstNum == None:
            firstNum = word[i]
        if word[i].isdigit():
            lastNum = word[i]

        for key, value in listOfNumbers.items():
            numWordLength = len(key)
            if word[i:i + numWordLength] == key and firstNum == None:
                firstNum = value
            if word[i:i + numWordLength] == key:
                lastNum = value
        
    totalSum += int(firstNum + lastNum)

print(totalSum)