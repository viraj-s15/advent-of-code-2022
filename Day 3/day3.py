from string import ascii_letters

filename = "Day 3/input.in"

data = open(filename).read().split('\n')
priority_map = {}
total_priority = 0

for strings in data:
    half_len = len(strings) // 2
    left_str = set(strings[:half_len])
    right_str = set(strings[half_len:])
    
    for priority,char in enumerate(ascii_letters):
        priority_map[char] = priority + 1

    for key,value in priority_map.items():
        if key in left_str and key in right_str:
            total_priority += value;     

upper = 3;
three_items = []
first,second,third = [], [] , []
three_sum = 0


for lower in range(0, len(data), 3):
    three_items = data[lower:upper]
    first,second,third = set(three_items[0]), set(three_items[1]),set(three_items[2])
    
    for key,value in priority_map.items():
        if key in first and key in second and key in third:
            three_sum += value;

    
    upper += 3
    
    
                
print("Solution to first part:", total_priority)    
print("Solution to second part:", three_sum)   

