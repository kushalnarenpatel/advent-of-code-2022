with open('day4-input.txt') as f:
    totalSum = 0
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        # split line into elf 1 and elf 2
        elfPair = line.split(",")
        elf1 = elfPair[0]
        elf2 = elfPair[1]

        # find upper and lower bounds of each elf's range
        # eg. 2-4 -> low = 2, high = 4
        elf1Ranges = elf1.split("-")
        elf1Low = int(elf1Ranges[0])
        elf1High = int(elf1Ranges[1])
        elf2Ranges = elf2.split("-")
        elf2Low = int(elf2Ranges[0])
        elf2High = int(elf2Ranges[1])

        # determine if one elf's range overlaps with the other's
        containFound = False
        if (elf1Low <= elf2Low):
            if (elf1High >= elf2Low):
                totalSum += 1
                containFound = True
        if (not containFound):
            if (elf2Low <= elf1Low):
                if (elf2High >= elf1Low):
                    totalSum +=1
    print(totalSum)