import math
import random
import pandas as pd

# Its your final turn in a heated game of Yahtzee,
# and the only combination of dice you still need to
# score is a large straight (when all five dice show
# numbers in sequential order): You want your five
# dice to eventually show 1, 2, 3, 4 and 5 or 2, 3,
# 4, 5 and 6. On the first of your three possible
# rolls during your final turn, you roll 1, 2, 4, 5
# and X (where X is not a 3). You could reroll the X
# in hopes of getting a 3. Or you could reroll the 1
# and the X in hopes that they eventually land in some
#  combination of 3 and 6. Or perhaps something
#  completely different!



def getRoll(number):
    """the method returns a list containing number results
    between 1 and 6."""
    result = []
    for die in range(number):
        roll = rand.randint(1, 6)
        result.append(roll)
    # print((n1, n2))
    return result

def scoreHand(hand):
    """takes a hand and evaluates it, returns a value for the hand"""
    if hand[3] == hand[4]:
        if hand[3] == 4:
            return 50
        return 25
    return sum(hand)

def playRollTwo(twice=False):
    """rolls 2 dice, evaluates new hand and rolls 0, 1, or 2 dice again
    returns score"""
    rollOne = getRoll(2)
    # print(rollOne)
    if rollOne[0] == 3:
        if (rollOne[1] == (1 or 6)):
            return 40
        elif (getRoll(1)[0] == (1 or 6)):
            return 40
        else:
            return 0
    elif rollOne[1] == 3:
        if (rollOne[0] == (1 or 6)):
            return 40
        elif (getRoll(1)[0] == (1 or 6)):
            return 40
        else:
            return 0
    elif twice:
        rollTwo = getRoll(2)
        # print(rollTwo)
        if rollTwo[0] == 3:
            if (rollTwo[1] == (1 or 6)):
                return 40
            else:
                return 0
        elif rollTwo[1] == 3:
            if (rollTwo[0] == (1 or 6)):
                return 40
            else:
                return 0
        else:
            return 0
    elif rollOne[0] == (1 or 6):
        if getRoll(1) == 3:
            return 40
        else:
            return 0
    elif rollOne[1] == (1 or 6):
        if getRoll(1) == 3:
            return 40
        else:
            return 0
    else:
        rollTwo = getRoll(2)
        # print(rollTwo)
        if rollTwo[0] == 3:
            if (rollTwo[1] == (1 or 6)):
                return 40
            else:
                return 0
        elif rollTwo[1] == 3:
            if (rollTwo[0] == (1 or 6)):
                return 40
            else:
                return 0
        else:
            return 0

def playRollOne():
    rollOne = getRoll(2)
    if rollOne[0] == 3 or rollOne[1] == 3:
        return 40
    else:
        return 0



def generateHand():
    """returns a hand consisting of 3 4's and 2 randomly generated numbers"""
    hand = [4, 4, 4]
    # print(hand)
    roll = getRoll()
    hand += roll
    return hand

def generateSample(size):
    """takes a sample size and generates a collection of that many scored hands """
    sample = pd.DataFrame(columns=['hand', 'score'])
    for trial in range(size):
        hand = generateHand()
        score = scoreHand(hand)
        tempdf = pd.DataFrame([[hand, score]], columns=['hand', 'score'])
        # print(tempdf)
        sample = sample.append(tempdf)
    sample.index = range(size)

    return sample


rand = random.Random()
rand.seed()
sampleSize = 100000
results = []
# sample = generateSample(sampleSize)
# print(sample['score'].mean())

for num in range(sampleSize):
    # results.append(playRollTwo(twice=True))
    results.append(playRollOne())

print(float(sum(results)/sampleSize))


