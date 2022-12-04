with open('day1-input.txt') as f:
    calorieTotals = []
    highestCalorieTotal = -1
    calorieTotal = 0
    lines = f.readlines()
 
    # iterate through each line in the input file
    for line in lines:
        # if the line is blank, it will only contain the newline character which has ASCII value 10
        if ((len(line) == 1) and (ord(line) == 10)):
            # as this is the end of an elf's items, store the sum of the calories of the items which this elf is carrying
            calorieTotals.append(calorieTotal)
            calorieTotal = 0
        else:
            # this line represents the calorie count of an item
            # increment calorieTotal by the number of calories which this item contains
            calorieTotal += int(line)
    # sort the list of total calories which each elf is carrying in ascending order and
    # return the sum of the last three elements of this list 
    print(sum(sorted(calorieTotals)[-3:]))