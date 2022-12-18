filename = "Day 7/input.in"
data = [data.strip() for data in open(filename).readlines()]

path = "/home"
directories = {"/home":0}

for command in data:
    if command[0] == "$":
        
        if command[2:4] == "ls":
            pass
        elif command[2:4] == "cd":
            if command[5:6] == "/":
                path = "/home"

            elif command[5:7] == "..":
                path = path[:path.rfind("/")]
                
            else:
                directory_name = command[5:]
                path = path + "/" + directory_name
                directories.update({path:0})
                
    elif command[:3] == "dir":
        pass
    
    else:
        file_size = int(command[:command.find(" ")])
        directory_name = path
        for i in range(path.count("/")):
            directories[directory_name] += file_size
            directory_name = directory_name[:directory_name.rfind("/")]


cost = 0

unused_space = 30000000 - (70000000 - directories["/home"])
directories_above_unused_space = []        
        
for key,value in directories.items():
    if value <+ 100000:
        cost += value
        
    if unused_space <= value:
        directories_above_unused_space.append(value)
        
    smallest = min(directories_above_unused_space)

print("Solution to part 1:", cost)
print("Solution to part 1:", smallest)

    