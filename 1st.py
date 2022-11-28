'''
Create a stats_finder() function that takes in a list of numbers
and returns a list containing the mean and mode, in that order.
If there are multiple modes, return the mode with the lowest value.
Make sure that you write your functions and find these answers from scratch – don’t use imported tools!
'''

def stats_finder(array):

    answers = []
    # Mean
    tot = 0
    count = 0
    for i in array:
        tot += i
        count += 1
    mean = tot / count
    answers.append(mean)

    # Mode
    numbers = {}
    counter = 0
    mode = None

    for num in array:
        if num not in numbers:
            numbers[num] = 0

    for key in numbers.keys():
        for num in array:
            if key == num:
                numbers[key] += 1

    for key, value in numbers.items():
        if mode == None:
            mode = key
            counter = value
        elif key < mode and value >= counter:
            mode = key
            counter = value

    answers.append(mode)
    return answers


print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))