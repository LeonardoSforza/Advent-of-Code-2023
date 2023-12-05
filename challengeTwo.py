from collections import defaultdict

file = open('data.txt', 'r')
data = file.read()
data = data.split("\n")

mapOfSeeds = defaultdict(list)
seeds = []

seedNumSplit = data[0].split(":")[1].strip().split(" ")
i = 0

print("Starting Seeds")

while i < len(seedNumSplit):
    if i % 2 == 0: # Even
        print("Even Num")
        startNum = int(seedNumSplit[i])
        for j in range(i, int(seedNumSplit[i+1])):
            seeds.append(int(startNum + j))
            mapOfSeeds[int(startNum + j)] = [int(startNum + j)]
            j +=1
    i += 1

print("Seeds done")

i = 1
while i < len(data):
    if data[i].split(":")[0] == "seed-to-soil map":
        print("Doing 1")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            soilNum = int(numbers[0])
            seedNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for key, value in mapOfSeeds.items():
                if (int(numbers[1]) + thirdNum) - key >= 0 and int(numbers[1]) <= key:
                    mapOfSeeds[key] = [(key - int(numbers[1])) + int(numbers[0])]
            i += 1
        
    
    if data[i].split(":")[0] == "soil-to-fertilizer map":
        print("Doing 2")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            fertNum = int(numbers[0])
            soilNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for key, value in mapOfSeeds.items():
                if len(value) == 2:
                    continue
                if (int(numbers[1]) + thirdNum) - value[0] >= 0 and int(numbers[1]) <= value[0]:
                    mapOfSeeds[key] = [value[0], (value[0] - int(numbers[1])) + int(numbers[0])]
            i += 1
        # Check for empty
        for key, value in mapOfSeeds.items():
            fertNum = value[0]
            if len(value) == 1:
                mapOfSeeds[key] = [value[0], value[0]]
            
    if data[i].split(":")[0] == "fertilizer-to-water map":
        print("Doing 3")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            waterNum = int(numbers[0])
            fertNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for key, value in mapOfSeeds.items():
                if len(value) == 3:
                    continue
                if (int(numbers[1]) + thirdNum) - value[1] >= 0 and int(numbers[1]) <= value[1]:
                    mapOfSeeds[key] = [value[0], value[1], (value[1] - int(numbers[1])) + int(numbers[0])]
            i += 1
        # Check for empty
        for key, value in mapOfSeeds.items():
            if len(value) == 2:
                mapOfSeeds[key] = [value[0], value[1], value[1]]

    if data[i].split(":")[0] == "water-to-light map":
        print("Doing 4")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            lightNum = int(numbers[0])
            waterNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for key, value in mapOfSeeds.items():
                if len(value) == 4:
                    continue
                if (int(numbers[1]) + thirdNum) - value[2] >= 0 and int(numbers[1]) <= value[2]:
                        mapOfSeeds[key] = [value[0], value[1], value[2], (value[2] - int(numbers[1])) + int(numbers[0])]
            i += 1
        # Check for empty
        for key, value in mapOfSeeds.items():
            if len(value) == 3:
                mapOfSeeds[key] = [value[0], value[1], value[2], value[2]]

    if data[i].split(":")[0] == "light-to-temperature map":
        print("Doing 5")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            tempNum = int(numbers[0])
            lightNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for key, value in mapOfSeeds.items():
                if len(value) == 5:
                    continue
                if (int(numbers[1]) + thirdNum) - value[3] >= 0 and int(numbers[1]) <= value[3]:
                        mapOfSeeds[key] = [value[0], value[1], value[2], value[3], (value[3] - int(numbers[1])) + int(numbers[0])]
            i += 1
        # Check for empty
        for key, value in mapOfSeeds.items():
            if len(value) == 4:
                mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[3]]

    if data[i].split(":")[0] == "temperature-to-humidity map":
        print("Doing 6")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            humNum = int(numbers[0])
            tempNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for key, value in mapOfSeeds.items():
                if len(value) == 6:
                    continue
                if (int(numbers[1]) + thirdNum) - value[4] >= 0 and int(numbers[1]) <= value[4]:
                        mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], (value[4] - int(numbers[1])) + int(numbers[0])]
            i += 1
        # Check for empty
        for key, value in mapOfSeeds.items():
            waterNum = value[4]
            if len(value) == 5:
                mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], value[4]]

    if data[i].split(":")[0] == "humidity-to-location map":
        print("Doing 7")
        i += 1
        while i < len(data):
            numbers = data[i].strip().split(" ")
            locNum = int(numbers[0])
            humNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for key, value in mapOfSeeds.items():
                if len(value) == 7:
                    continue
                if (int(numbers[1]) + thirdNum) - value[5] >= 0 and int(numbers[1]) <= value[5]:
                        mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], value[5], (value[5] - int(numbers[1])) + int(numbers[0])]
            i += 1
        # Check for empty
        for key, value in mapOfSeeds.items():
            waterNum = value[5]
            if len(value) == 6:
                mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], value[5], value[5]]
    i += 1

minLocation = None
for key, value in mapOfSeeds.items():
    if minLocation == None:
        minLocation = mapOfSeeds[key][-1]
    if mapOfSeeds[key][-1] < minLocation:
        minLocation = mapOfSeeds[key][-1]
print(minLocation)