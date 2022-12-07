with open('day3-input.txt', 'r', encoding="utf-8") as f:
    totalSum = 0
    lines = f.readlines()
    # check each elf's rucksack
    for line in lines:
        # split the rucksack contents up into the two compartments
        n = len(line) // 2
        compartment1 = line[:n]
        compartment2 = line[n:]
        dict1 = {}
        value = 0
        # store the items in compartment 1 and their values
        for item in compartment1:
            if item.isupper():
                value = ord(item) - ord("A") + 27
            else:
                value = ord(item) - ord("a") + 1
            dict1[item] = value
        # if an item exists in both compartments, increment total by its value
        for item in compartment2:
            if item in dict1:
                print(dict1[item])
                totalSum += dict1[item]
                break
            # print total of the values of items shared across compartments
    print(totalSum)