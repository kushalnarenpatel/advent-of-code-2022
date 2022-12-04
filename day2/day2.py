import sys

with open('day2-input.txt', 'r', encoding="utf-8") as f:
    totalScore = 0
    elfScoreMap = {"A":1, "B":2, "C":3}
    playerScoreMap = {"X":1,"Y":2,"Z":3}
    gameResultMap = {"X":"L","Y":"D","Z":"W"}
    # rock                lose
    # paper               draw
    # scissors            win
    lines = f.readlines()
    for line in lines:
        elfChoice, gameChoice = line.rstrip().split(" ")
        elfScore = elfScoreMap[elfChoice]
        gameResult = gameResultMap[gameChoice]
        if (gameResult == "D"):
            totalScore += 3 + elfScore
        else:
            if (elfScore == 1):
                if (gameResult == "L"):
                    totalScore += 3
                else:
                    totalScore += 6 + 2
            elif (elfScore == 2):
                if (gameResult == "L"):
                    totalScore += 1
                else:
                    totalScore += 6 + 3
            else:
                if (gameResult == "L"):
                    totalScore += 2
                else:
                    totalScore += 6 + 1
    print(totalScore)

        # print(playerScore, elfScore)
        # if ((playerScore == 1) and (elfScore == 3) or (playerScore == 3) and (elfScore == 2) 
        # or ((playerScore == 2) and (elfScore == 1))):
        #     totalScore += 6 + playerScore
        # elif (playerScore == elfScore):
        #     totalScore += 3 + playerScore
        # else:
        #     totalScore += playerScore
    print(totalScore)