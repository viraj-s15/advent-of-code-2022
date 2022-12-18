from collections import defaultdict

filename = "Day 14/input.in"

f = open(filename).read().strip().split("\n")

start = (500,0)

rocks = set()

horizontal_rows = []


row_map = defaultdict(list)

for path in f:
    x_and_y = []
    spots = path.split(" -> ")
    for spot in spots:
        q = spot.split(",")
        x,y = int(q[0]), int(q[1])
        x_and_y.append((x,y))
    for (x1,y1), (x2, y2) in zip(x_and_y[:-1], x_and_y[1:]):
        for tempx in range(min(x1, x2), max(x1, x2) + 1):
            for tempy in range(min(y1, y2), max(y1, y2) + 1):
                row_map[tempy].append(tempx)
                rocks.add((tempx, tempy))
        if max(x1, x2) - min(x1, x2) >= 2 and y1 == y2:
            horizontal_rows.append((min(x1, x2), max(x1, x2), y1))


sand = set()

lowest_rock = max(x[1] for x in rocks)

def check_bottom(pos):
    return (pos[0], pos[1] + 1) in rocks or (pos[0], pos[1] + 1) in sand

def check_bottom_right(pos):
    return (pos[0] + 1, pos[1] + 1) in sand or (pos[0] + 1, pos[1] + 1) in rocks

def check_bottom_left(pos):
    return (pos[0] - 1, pos[1] + 1) in sand or (pos[0] - 1, pos[1] + 1) in rocks



height = lowest_rock + 2
def find_path(p1):
    if not p1:
        for i in range(500 - height * 2, 500 + height * 2):
            rocks.add((i, lowest_rock + 2))
    placed = False
    while not placed:

        if (500, 0) in sand:
            placed = True
        not_placed = True
        new_sand = start
        while not_placed:
            if check_bottom(new_sand):
                if check_bottom_left(new_sand):
                    if check_bottom_right(new_sand):
                        sand.add(new_sand)
                        not_placed = False
                    else:
                        new_sand = (new_sand[0] + 1, new_sand[1])
                else:
                    new_sand = (new_sand[0] - 1, new_sand[1])
            new_sand = (new_sand[0], new_sand[1] + 1)
            if new_sand[1] > lowest_rock + 2 * (0 if p1 else 1):
                placed = True
                break
    return len(sand)

def triangles():
    all_sand = set()
    m1, m2 = 500, 500
    for i in range(lowest_rock + 2):
        for j in range(m1, m2 + 1):
            all_sand.add((j,i))
        m1 -= 1
        m2 += 1
    all_sand = all_sand.difference(rocks)
    def ranges(nums):
        nums = sorted(set(nums))
        gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
        edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
        return list(filter(lambda x: x[-1] - x[0] >= 2, list(zip(edges, edges))))
    horizontal_rows = []
    blocked_by_rows = set()
    while True:
        before = len(blocked_by_rows)
        for row, places in row_map.items():
            asdf = ranges(places)
            for a in asdf:
                horizontal_rows.append((a[0], a[1], row))
        for l, r, h in horizontal_rows:
            templ, tempr, temph = l+1, r, h+1
            while templ <= tempr:
                for q in range(templ, tempr):
                    rocks.add((q, temph))
                    blocked_by_rows.add((q, temph))
                    row_map[temph].append(q)
                templ += 1
                tempr -= 1
                temph += 1
        after = len(blocked_by_rows)
        if after == before:
            break

    all_sand = all_sand.difference(blocked_by_rows)
    return len(all_sand)

print("Solution to Part 1:", find_path(True))
print("Solution to part 2:", triangles())
