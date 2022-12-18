file_path = 'Day 1/input.in'

data_set = open(file_path, "r").read().split("\n\n")
maximum_cal = 0
sorted_array = []



for i in data_set:
    maximum_cal = max(maximum_cal,sum([int(r) for r in i.splitlines()]))
    sorted_array.append(sum(int(j) for j in i.splitlines()))
    
sorted_array = sorted(sorted_array)
    
print("Part 1 solution:", maximum_cal)
print("Part 2 solution:", sum(sorted_array[-3:]))


    
    
    
    
    
    
    