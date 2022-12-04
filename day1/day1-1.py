import sys

with open('day1-input.txt', 'r', encoding="utf-8") as f:
    calorieTotals = []
    highestCalorieTotal = -1
    calorieTotal = 0
    lines = f.readlines()

    for line in lines:
        # print(len(line))
        if len(line) == 1:
            calorieTotals.append(calorieTotal)
            if calorieTotal > highestCalorieTotal:
                highestCalorieTotal = calorieTotal
            calorieTotal = 0
                # print("reset")
        else:
            calorieTotal += int(line)
            # print(calorieTotal)
    calorieTotals.append(calorieTotal)
    print(sum(sorted(calorieTotals)[-3:]))