filename = "Day 9/input.in"

data = open(filename)

output = set([(0,0)])

head = [0, 0]
tail = [0, 0]

for line in open(filename):
    direction, step = line.split()
    step = int(step)

    for _ in range(step):
        change_in_x = 1 if direction == "R" else -1 if direction == "L" else 0
        change_in_y = 1 if direction == "U" else -1 if direction == "D" else 0

        head[0] += change_in_x
        head[1] += change_in_y

        change_in_x1 = head[0] - tail[0]
        change_in_y1 = head[1] - tail[1]

        if abs(change_in_x1) > 1 or abs(change_in_y1) > 1:
            if change_in_x1 == 0:
                tail[1] += change_in_y1 // 2
            elif change_in_y1 == 0:
                tail[0] += change_in_x1 // 2
            else:
                tail[0] += 1 if change_in_x1 > 0 else -1
                tail[1] += 1 if change_in_y1 > 0 else -1
        
        output.add(tuple(tail))

output1 = set([(0, 0)])

R = [[0, 0] for _ in range(10)]

for line in open(filename):
    direction1, step1 = line.split()
    step1 = int(step1)

    for _ in range(step1):
        change_in_x = 1 if direction1 == "R" else -1 if direction1 == "L" else 0
        change_in_y = 1 if direction1 == "U" else -1 if direction1 == "D" else 0

        R[0][0] += change_in_x
        R[0][1] += change_in_y

        for i in range(9):
            head1 = R[i]
            tail1 = R[i + 1]

            change_in_x1 = head1[0] - tail1[0]
            change_in_y1 = head1[1] - tail1[1]

            if abs(change_in_x1) > 1 or abs(change_in_y1) > 1:
                if change_in_x1 == 0:
                    tail1[1] += change_in_y1 // 2
                elif change_in_y1 == 0:
                    tail1[0] += change_in_x1 // 2
                else:
                    tail1[0] += 1 if change_in_x1 > 0 else -1
                    tail1[1] += 1 if change_in_y1 > 0 else -1

        output1.add(tuple(R[-1]))

print("Solution to part 1:",len(output))
print("Solution to part 2:",len(output1))


