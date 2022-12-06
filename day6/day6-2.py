with open('day6-input.txt') as f:
    input = f.readlines()[0]

    # set up sliding window
    charWindow = []
    start = 0
    end = 0

    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    # ^                                ^
    # iterate through each characters in the input string
    for i in range(len(input)):
        # when sliding window has length 14, check if it contains 4 unique characters
        if (end - start == 14):
            if (len(set(charWindow)) == 14):
                # if it does, print the index of the start pointer and end execution
                print(i)
                break
            charWindow.remove(input[start])
            start += 1
        charWindow.append(input[end])
        end += 1