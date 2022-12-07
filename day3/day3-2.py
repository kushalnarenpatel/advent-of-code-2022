with open('day3-input.txt', 'r', encoding="utf-8") as f:
    totalSum = 0
    lines = f.readlines()
    # examine each group of 3 elves' rucksacks
    for i in range(0, len(lines), 3):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        subLine = lines[i].rstrip()
        # for each item in the first elf's rucksack...
        for char in subLine:
            if char not in dict1:
                dict1[char] = True
        for char in lines[i + 1]:
            # if it's in the second elf's rucksack...
            if char in dict1:
                dict2[char] = True
        for char in lines[i + 2]:
            # and in the third elf's rucksack...
            if char in dict2:
                # then add its value to the total
                if char.isupper():
                    totalSum += ord(char) - ord("A") + 27
                else:
                    totalSum += ord(char) - ord("a") + 1
                break
    # print the total value of the badges of each group
    print(totalSum)