import sys

with open("input.txt", "r") as f:
    movementsList = f.readlines()
    #measurements = list(map(int, measurements))


# Part 1
if sys.argv[1] == "1":
    forward = 0
    depth = 0

    for line in movementsList:
        directions = line.split()
        directions[1] = int(directions[1])

        if directions[0] == "forward":
            forward += directions[1]
        if directions[0] == "up":
            depth -= directions[1]
        if directions[0] == "down":
            depth += directions[1]
    print(forward * depth)

# Part 2
if sys.argv[1] == "2":
    forward = 0
    depth = 0
    aim = 0

    for line in movementsList:
        directions = line.split()
        directions[1] = int(directions[1])

        if directions[0] == "forward":
            forward += directions[1]
            depth += aim * directions[1]
        if directions[0] == "up":
            aim -= directions[1]
        if directions[0] == "down":
            aim += directions[1]

    print(forward * depth)
