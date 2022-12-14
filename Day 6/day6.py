from collections import Counter


filename = "/home/veer/Documents/advent-of-code/Day 6/input.in"

data = open(filename).read()

for i in range(4,len(data)):
    characters = data[i-4:i]
    frequency = Counter(characters)
    if (len(frequency) == len(characters)):
        print("Solution to part 1:", i)
        break;

for i in range(14,len(data)):
    characters = data[i-14:i]
    frequency = Counter(characters)
    if (len(frequency) == len(characters)):
        print("Solution to part 2:", i)
        break;
    
    