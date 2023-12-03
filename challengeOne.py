file = open('data.txt', 'r')
data = file.read()

matrix = data.split("\n")

totalSum = 0

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
                didYouFind = False
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
                    if matrix[y][copyStartNumIndex] == "#" or matrix[y][copyStartNumIndex] == "*" or matrix[y][copyStartNumIndex] == "+" or matrix[y][copyStartNumIndex] == "$" or matrix[y][copyStartNumIndex] == "-" or matrix[y][copyStartNumIndex] == "@" or matrix[y][copyStartNumIndex] == "=" or matrix[y][copyStartNumIndex] == "/" or matrix[y][copyStartNumIndex] == "%" or matrix[y][copyStartNumIndex] == "&":
                        totalSum += int(numValue)
                        didYouFind = True
                        break
                    copyStartNumIndex += 1
                
                if didYouFind:
                    break

        j += 1

print(totalSum)