from  parse import parse
from tqdm import tqdm, trange

filename: str = "Day 15/input.in "

f = open(filename).read().strip().split("\n")

def final_distance(x,y, q,w):
    return abs(q-x) + abs(w - y)

distance = {}

beacons = set()
min_x = 1000000000
max_x = -10000000
max_distance = 0
for instruction in f:
    x,y, q,w = parse("Sensor at x={:distance}, y={:distance}: closest beacon is at x={:distance}, y={:distance}", instruction)
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    dist = final_distance(x,y,q,w)
    distance[(x,y)] = dist
    beacons.add((q,w))
    max_distance = max(max_distance, dist)

spots = 0
for i in trange(min_x - max_distance, max_x + max_distance + 1):
    near_sensor = False
    for point, dist in distance.items():
        if final_distance(point[0], point[1], i, 2000000) <= dist and (i, 2000000) not in beacons:
            near_sensor = True
            break
    if near_sensor:
        spots += 1
print("Solution to part 1:",spots)


def outside(point, dist, m_in, m_ax):
    x,y = point
    p = dist + 1
    q = 0

    result = set()
    while p >= 0:
        if m_in <= x + p <= m_ax and m_in <= y + q <= m_ax and final_distance(x, y, (x+p), (y + q)) == dist + 1:
            result.add((x+p, y+q))
        if m_in <= x - p <= m_ax and m_in <= y - q <= m_ax and final_distance(x, y, (x - p), (y - q)) == dist + 1:
            result.add((x - p, y - q))
        if m_in <= x - p <= m_ax and m_in <= y + q <= m_ax and final_distance(x, y, (x - p), (y + q)) == dist + 1:
            result.add((x - p, y + q))
        if m_in <= x + p <= m_ax and m_in <= y - q <= m_ax and final_distance(x, y, (x + p), (y - q)) == dist + 1:
            result.add((x + p, y - q))
        p -= 1
        q += 1
    return list(result)

immediate_outside = []
for point, dist in tqdm(distance.items()):
    immediate_outside.extend(outside(point, dist, 0, 4000000))
for x,y in tqdm(immediate_outside):
    near_sensor = False
    for point, dist in distance.items():
        if final_distance(point[0], point[1], x, y) <= dist and (x, y) not in beacons:
            near_sensor = True
            break
    if not near_sensor and (x,y) not in beacons:
        print(x*4000000 + y)
        break