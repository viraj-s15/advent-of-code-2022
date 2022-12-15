filename = "Day 10/input.in"

data = open(filename).read()

x = [1, 1]
count = 0
for value in data.splitlines():
    match value.split():
        case ["noop"]:
            x.append(x[-1])
        case ["addx", num]:
            x.append(x[-1])
            x.append(x[-1] + int(num))

print("Solution to part 1:",sum(i * x[i] for i in (20, 60, 100, 140, 180, 220)))

for i in range(6):
    for j in range(40):
        hash_symbol = x[i * 40 + j + 1]
        print("#" if j in (hash_symbol - 1, hash_symbol, hash_symbol + 1) else ".", end="")
    print()