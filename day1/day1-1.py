with open('day1-input.txt') as f:
    calorieTotals = []
    highestCalorieTotal = -1
    calorieTotal = 0
    lines = f.readlines()

    # iterate through each line in the input file
    for line in lines:
        # if the line is blank, it will only contain the newline character which has ASCII value 10
        if ((len(line) == 1) and (ord(line) == 10)):
            # check if the sum of calories of the items which this elf is carrying is greater 
            # than the current highest sum of calories found
            if calorieTotal > highestCalorieTotal:
                highestCalorieTotal = calorieTotal
            calorieTotal = 0
        else:
            # this line represents the calorie count of an item
            # increment calorieTotal by the number of calories which this item contains
            calorieTotal += int(line)
    # return the highest calorie count found
    print(highestCalorieTotal)