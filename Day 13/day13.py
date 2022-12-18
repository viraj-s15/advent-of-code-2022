import functools
import ast
from math import prod

filename = "Day 13/input.in"

data = open(filename).read().strip().split("\n\n")


def compare(left, right):
    if type(left) == type(right):
        if type(left) == int:
            if left == right:
                return "k"
            else:
                return left < right
        else:
            for left2, right2 in zip(left, right):
                ok = compare(left2, right2)
                if not ok:
                    return False
                if ok is True:
                    return True
            if len(left) < len(right):
                return True
            if len(right) < len(left):
                return False
        return "k"
    else:
        if type(right) == list:
            return compare([left], right)
        if type(left) == list:
            return compare(left, [right])


def comp2(x, y):
    return - 1 * compare(x, y)


valid = 0
lines = []
for i, pair in enumerate(data):
    first, second = pair.split("\n")
    first = ast.literal_eval(first)
    second = ast.literal_eval(second)
    lines.append(first)
    lines.append(second)
    if compare(first, second):
        valid += (i + 1)
        
        
lines.append([[2]])
lines.append([[6]])
al = sorted(lines, key=functools.cmp_to_key(comp2))
print("Solution to part1:",valid)
print("Solution to part2:",prod(i for i, line in enumerate(al, 1) if line in [[[2]], [[6]]]))