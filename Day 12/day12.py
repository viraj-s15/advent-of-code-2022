from heapq import heappop, heappush
from string import ascii_lowercase
from collections import deque

filename = "Day 12/input.in"

with open(filename) as f:
    lines = f.read().strip().split()

graph = [list(line) for line in lines]
col = len(graph)
row = len(graph[0])


for i in range(col):
    for j in range(row):
        char = graph[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j


def get_elevation(char):
    if char in ascii_lowercase:
        return ascii_lowercase.index(char)
    if char == "S":
        return 0
    if char == "E":
        return 25



def find_neighbours(i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < col and 0 <= jj < row):
            continue

        if get_elevation(graph[ii][jj]) <= get_elevation(graph[i][j]) + 1:
            yield ii, jj




visited = [[False] * row for _ in range(col)]
heap = [(0, start[0], start[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    if (i, j) == end:
        print(steps)
        break

    for k, l in find_neighbours(i, j):
        heappush(heap, (steps + 1, k, l))
        

grid = [list(x) for x in open(filename).read().strip().splitlines()]

for row1, row in enumerate(grid):
    for col1, item in enumerate(row):
        if item == "S":
            grid[row1][col1] = "a"
        if item == "E":
            ec = col1
            er = row1
            grid[row1][col1] = "z"

# part 2
queue = deque()
queue.append((0, er, ec))

visible = {(er, ec)}

while queue:
    d, row1, col1 = queue.popleft()
    for nrow, ncol in [(row1 + 1, col1), (row1 - 1, col1), (row1, col1 + 1), (row1, col1 - 1)]:
        if nrow < 0 or ncol < 0 or nrow >= len(grid) or ncol >= len(grid[0]):
            continue
        if (nrow, ncol) in visible:
            continue
        if ord(grid[nrow][ncol]) - ord(grid[row1][col1]) < -1:
            continue
        if grid[nrow][ncol] == "a":
            print(d + 1)
            exit()
        queue.append((d + 1, nrow, ncol))
        visible.add((nrow, ncol))