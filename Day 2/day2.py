
file_path = "/home/veer/Documents/advent-of-code/Day 2/input.in"

array = []

data_set = open(file_path, 'r').read().split("\n")


result = {
    'A X' : 4,
    'A Y' : 8,
    'A Z' : 3,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 7,
    'C Y' : 2,
    'C Z' : 6,
}

result2 = {
    'A X' : 3,
    'A Y' : 4,
    'A Z' : 8,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 2,
    'C Y' : 6,
    'C Z' : 7,
}

total_cost = 0

for pair in data_set:
    total_cost += result[pair]

total_cost_revised = 0

for pair in data_set:
    total_cost_revised += result2[pair]



print("Solution to part 1:", total_cost)    
print("Solution to part 2:", total_cost_revised)    

    
    