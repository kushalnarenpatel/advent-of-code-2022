import re

with open('day5-input.txt') as f:
    lines = f.readlines()
    numStacks = 0
    lineBreakIndex = 0
    # find the number of supply stacks
    for i in range(len(lines)):
        # if the line is blank, it will only contain the newline character which has ASCII value 10
        # if we find a blank line, we know that we have reached the end of the supply stacks information
        if ((len(lines[i]) == 1) and (ord(lines[i]) == 10)):
            numStacks = max(list(map(int,(lines[i - 1].split("   ")))))
            lineBreakIndex = i
            break
    
    # instantiate a list of stacks, whose length equals the number of supply stacks
    stackList = []
    for i in range(numStacks):
        stack = []
        stackList.append(stack)

    # load the state of the supply stacks into the stack objects
    for i in range(lineBreakIndex, -1, -1):
        line = lines[i]
        for i in range(len(line)):
            if (ord("A") <= ord(line[i]) <= ord("Z")):
                stackList[i // 4].append(line[i])

    # conduct moves
    for i in range(lineBreakIndex, len(lines)):
        # parse line to find how many crates we are moving and their source + destination
        line = lines[i]
        numsFound = re.findall("\d+", line)
        if (len(numsFound) > 0):
            moveNo = int(numsFound[0])
            moveFrom = int(numsFound[1]) - 1
            moveTo = int(numsFound[2]) - 1
            for j in range(moveNo):
                # move crates
                stackList[moveTo].append(stackList[moveFrom].pop())

    # print crate on top of each stack
    outString = ""
    for stack in stackList:
        outString += stack.pop()
    print(outString)