from math import lcm, prod
import re
from typing import ClassVar

filename = "Day 11/input.in"

matches = re.compile(r"\d+")

data = open(filename).read()

class MonkeyOperations:
    inspections: int = 0
    lcm: ClassVar[int] = 1

    def __init__(self, input: str):
        _, number_of_items, operation, test, if_true, if_false = input.splitlines()
        self.number_of_items = [int(i) for i in matches.findall(number_of_items)]
        self.operation = lambda old: eval(operation.split("=")[1])
        self.test = int(matches.findall(test)[0])
        self.throw_if_true = int(matches.findall(if_true)[0])
        self.throw_if_false = int(matches.findall(if_false)[0])
        MonkeyOperations.lcm = lcm(MonkeyOperations.lcm, self.test)

    def turn(self, monkeys, part1: bool):
        while self.number_of_items:
            self.inspections += 1
            worry = self.operation(self.number_of_items.pop(0)) % self.lcm
            if part1:
                worry = worry // 3
            recipient = self.throw_if_true if worry % self.test == 0 else self.throw_if_false
            monkeys[recipient].number_of_items.append(worry)



def create_array(data):
    return [MonkeyOperations(s) for s in data.split("\n\n")]

monkeys = create_array(data)

for round in range(20):
    for monkey in monkeys:
        monkey.turn(monkeys, True)
print(prod(sorted(m.inspections for m in monkeys)[-2:]))

monkeys = create_array(data)

for round in range(10000):
    for monkey in monkeys:
        monkey.turn(monkeys, False)
print(prod(sorted(m.inspections for m in monkeys)[-2:]))