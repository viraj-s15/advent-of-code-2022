filename = "/home/veer/Documents/advent-of-code/Day 5/input.in"

with open(filename) as f:
    stacks, instructions = (i.splitlines() for i in f.read().strip("\n").split("\n\n"))

stack_map = {int(i):[] for i in stacks[-1].replace(" ", "")}
indices = [i for i,char in enumerate(stacks[-1]) if char != " "]

def load_stack():
    for string in stacks[:-1]:
        stack_num = 1
        for i in indices:
            if string[i] != " ":
                stack_map[stack_num].insert(0, string[i])
            stack_num += 1

def clear_stack():
    for stack_num in stack_map:
        stack_map[stack_num].clear()
        
        
load_stack()

def get_stack_end():
    answer = ""
    for stack in stack_map:
        answer += stack_map[stack][-1]
    return answer

for instruction in instructions:
    instruction = instruction.strip().replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]
    
    crate_name = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(0,crate_name):
        crate_removed = stack_map[from_stack].pop()
        stack_map[to_stack].append(crate_removed)

print("Solution for part 1:", get_stack_end())

clear_stack()
load_stack()

for instruction in instructions:
    instruction = instruction.strip().replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]
    
    crate_name = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    
    creates_to_remove = stack_map[from_stack][-crate_name:]
    stack_map[from_stack] = stack_map[from_stack][:-crate_name]
    
    for crate in creates_to_remove:
        stack_map[to_stack].append(crate)


print("Solution for part 2:", get_stack_end())
