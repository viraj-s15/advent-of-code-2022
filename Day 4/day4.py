filename = "Day 4/input.in"

data = open(filename, "r").read().split("\n")

number_of_pairs = 0
number_of_pairs_overlap = 0

for pair in data:
    first,second = pair.split(",");
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]
    
    if first[0] <= second[0] and first[1] >= second[1]:
        number_of_pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]:         
        number_of_pairs += 1
        
    if first[0] in range(second[0], second[1] + 1) or first[1] in range(second[0], second[1] + 1):
        number_of_pairs_overlap += 1
    elif second[0] in range(first[0], first[1] + 1) or second[1] in range(first[0], first[1] + 1):
        number_of_pairs_overlap += 1
        
        
print("Solution to the first part:",number_of_pairs)
print("Solution to the second part:",number_of_pairs_overlap)