from collections import defaultdict

file = open('data.txt', 'r')
data = file.read()

matrix = data.split("\n")

mapOfGears = defaultdict(list)

for i in range(0, len(matrix)):
    j = 0
    while j < len(matrix[i]):
        if matrix[i][j].isdigit():
            startNumIndex = j
            while matrix[i][j].isdigit():
                j += 1
                if j == len(matrix[i]):
                    break
            numValue = matrix[i][startNumIndex:j]
            
            coppyI = i - 1
            startNumIndex -= 1

            copyStartNumIndex = startNumIndex
            
            for y in range(coppyI, coppyI + 3):
                if y == len(matrix):
                    break
                if y < 0:
                    continue
                copyStartNumIndex = startNumIndex
                while copyStartNumIndex < j + 1:
                    if copyStartNumIndex == len(matrix[i]):
                        break
                    if copyStartNumIndex < 0:
                        copyStartNumIndex += 1
                        continue
                    if matrix[y][copyStartNumIndex] == "*":
                        mapOfGears[str(y) + ", " + str(copyStartNumIndex)].append(numValue)
                        break
                    copyStartNumIndex += 1

        j += 1

# print(mapOfGears)
sumGear = 0
for key, value in mapOfGears.items():
    if len(value) > 1:
        multiplyGear = 1
        for num in value:
            multiplyGear *= int(num)
        sumGear += multiplyGear

print(sumGear)