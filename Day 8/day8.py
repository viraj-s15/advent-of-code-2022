filename = "/home/veer/Documents/advent-of-code/Day 8/input.in"


data_list = [list(map(int,i)) for i in open(filename).read().splitlines()]

visible_trees = 0

visibility_score = 0

for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        current = data_list[i][j]
        if all(data_list[i][x] < current for x in range(j)) or all(data_list[i][x] < current for x in range(j + 1, len(data_list[i]))) or all(data_list[x][j] < current for x in range(i)) or all(data_list[x][j] < current for x in range(i + 1, len(data_list))):
            visible_trees += 1


for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        current = data_list[i][j]
        left = right = up = down = 0
        
        for x in range(i - 1, -1 , -1):
            up += 1
            if data_list[x][j] >= current:
                break
        for x in range(i + 1, len(data_list)):
            down += 1
            if data_list[x][j] >= current:
                break
            
        for x in range(j - 1, -1 , -1):
            left += 1
            if data_list[i][x] >= current:
                break
        for x in range(j + 1, len(data_list[i])):
            right += 1
            if data_list[i][x] >= current:
                break
        
        visibility_score = max(visibility_score, up * down * left * right)


print("Solution to part 1:", visible_trees)
print("Solution to part 2:", visibility_score)