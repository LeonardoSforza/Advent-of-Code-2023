from collections import defaultdict

file = open('data.txt', 'r')
data = file.read()
data = data.split("\n")

mapOfSeeds = defaultdict(list)
seeds = []

for seed in data[0].split(":")[1].strip().split(" "):
    seed = int(seed)
    seeds.append(seed)
    mapOfSeeds[seed] = [seed]

i = 1
while i < len(data):
    if data[i].split(":")[0] == "seed-to-soil map":
        print("Doing 1...")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            soilNum = int(numbers[0])
            seedNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for j in range(0, thirdNum):
                if seedNum+j in seeds:
                    mapOfSeeds[seedNum+j] = [soilNum+j]
            i += 1
        
    
    if data[i].split(":")[0] == "soil-to-fertilizer map":
        print("Doing 2...")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            fertNum = int(numbers[0])
            soilNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for j in range(0, thirdNum):
                for key, value in mapOfSeeds.items():
                    if value[0] == soilNum+j:
                        mapOfSeeds[key] = [value[0], fertNum+j]
            # Check for empty
            for key, value in mapOfSeeds.items():
                fertNum = value[0]
                if len(value) == 1:
                    mapOfSeeds[key] = [value[0], value[0]]
            i += 1

    if data[i].split(":")[0] == "fertilizer-to-water map":
        print("Doing 3...")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            waterNum = int(numbers[0])
            fertNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for j in range(0, thirdNum):
                for key, value in mapOfSeeds.items():
                    if value[1] == fertNum+j:
                        mapOfSeeds[key] = [value[0], value[1], waterNum+j]
            # Check for empty
            for key, value in mapOfSeeds.items():
                waterNum = value[1]
                if len(value) == 2:
                    mapOfSeeds[key] = [value[0], value[1], value[1]]
            i += 1

    if data[i].split(":")[0] == "water-to-light map":
        print("Doing 4...")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            lightNum = int(numbers[0])
            waterNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for j in range(0, thirdNum):
                for key, value in mapOfSeeds.items():
                    if value[2] == waterNum+j:
                        mapOfSeeds[key] = [value[0], value[1], value[2], lightNum+j]
            # Check for empty
            for key, value in mapOfSeeds.items():
                waterNum = value[2]
                if len(value) == 3:
                    mapOfSeeds[key] = [value[0], value[1], value[2], value[2]]
            i += 1

    if data[i].split(":")[0] == "light-to-temperature map":
        print("Doing 5...")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            tempNum = int(numbers[0])
            lightNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for j in range(0, thirdNum):
                for key, value in mapOfSeeds.items():
                    if value[3] == lightNum+j:
                        mapOfSeeds[key] = [value[0], value[1], value[2], value[3], tempNum+j]
            # Check for empty
            for key, value in mapOfSeeds.items():
                waterNum = value[3]
                if len(value) == 4:
                    mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[3]]
            i += 1

    if data[i].split(":")[0] == "temperature-to-humidity map":
        print("Doing 6...")
        i += 1
        while data[i] != "":
            numbers = data[i].strip().split(" ")
            humNum = int(numbers[0])
            tempNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for j in range(0, thirdNum):
                for key, value in mapOfSeeds.items():
                    if value[3] == tempNum+j:
                        mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], humNum+j]
            # Check for empty
            for key, value in mapOfSeeds.items():
                waterNum = value[4]
                if len(value) == 5:
                    mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], value[4]]
            i += 1

    if data[i].split(":")[0] == "humidity-to-location map":
        print("Doing 7...")
        i += 1
        while i < len(data):
            numbers = data[i].strip().split(" ")
            locNum = int(numbers[0])
            humNum = int(numbers[1])
            thirdNum = int(numbers[2])
            for j in range(0, thirdNum):
                for key, value in mapOfSeeds.items():
                    if value[3] == humNum+j:
                        mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], value[5], locNum+j]
            # Check for empty
            for key, value in mapOfSeeds.items():
                waterNum = value[5]
                if len(value) == 6:
                    mapOfSeeds[key] = [value[0], value[1], value[2], value[3], value[4], value[5], value[5]]
            i += 1
    i += 1

minLocation = None
for key, value in mapOfSeeds.items():
    if minLocation == None:
        minLocation = mapOfSeeds[key][-1]
    if mapOfSeeds[key][-1] < minLocation:
        minLocation = mapOfSeeds[key][-1]
print(minLocation)