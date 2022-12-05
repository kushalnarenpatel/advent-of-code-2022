import sys

with open('day2-input.txt', 'r', encoding="utf-8") as f:
    totalScore = 0

    # map each choice (rock, paper or scissors) to a score
    elfScoreMap = {"A":1, "B":2, "C":3}
    playerScoreMap = {"X":1,"Y":2,"Z":3}
    lines = f.readlines()

    # sum the elf's score from each move 
    for line in lines:
        print(totalScore)
        elfChoice, playerChoice = line.rstrip().split(" ")
        elfScore = elfScoreMap[elfChoice]
        playerScore = playerScoreMap[playerChoice]
        # determine the score for the move based on the move which the player and elf take
        # if the player and elf make the same move...
        if (playerScore == elfScore):
            totalScore += elfScore
        else:
            # if the elf chooses rock...
            if (elfScore == 1):
                if (playerScore == 2):
                    totalScore += 6 + playerScore
                else:
                    totalScore += playerScore
            # if the elf chooses paper...
            elif (elfScore == 2):
                if (playerScore == 1):
                    totalScore += 6 + playerScore
                else:
                    totalScore += playerScore
            # if the elf chooses scissors...
            else:
                if (playerScore == 3):
                    totalScore += 6 + playerScore
                else:
                    totalScore += playerScore
    # print the elf's total score
    print(totalScore)