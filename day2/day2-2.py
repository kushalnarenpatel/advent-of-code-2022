import sys

with open('day2-input.txt', 'r', encoding="utf-8") as f:
    totalScore = 0

    # map each choice (rock, paper or scissors) to a score
    elfScoreMap = {"A":1, "B":2, "C":3}
    gameResultMap = {"X":"L","Y":"D","Z":"W"}
    lines = f.readlines()

    # sum the elf's score from each move 
    for line in lines:
        elfChoice, gameChoice = line.rstrip().split(" ")
        elfScore = elfScoreMap[elfChoice]
        # determine what move the elf will make based on the outcome that needs to occur from the move (win, lose, draw)
        gameResult = gameResultMap[gameChoice]
        if (gameResult == "D"):
            totalScore += 3 + elfScore
        else:
            # if the elf chooses rock...
            if (elfScore == 1):
                if (gameResult == "L"):
                    totalScore += 3
                else:
                    totalScore += 6 + 2
            # if the elf chooses paper...
            elif (elfScore == 2):
                if (gameResult == "L"):
                    totalScore += 1
                else:
                    totalScore += 6 + 3
            # if the elf chooses scissors...
            else:
                if (gameResult == "L"):
                    totalScore += 2
                else:
                    totalScore += 6 + 1
    # print the elf's total score
    print(totalScore)