import math
import random
import pandas as pd

# so what are we doing?
# Suppose that youre playing a one-turn game of Yahtzee,
#  in which your only consideration is maximizing your score
# on this single turn. (In Yahtzee, a player has up to three
# rolls of five dice to get various combinations of numbers,
#  which earn the player different numbers of points.) After
#  your second of three rolls, your five dice show 4, 4, 4, 5
#  and 5. You could keep all of your dice and score 25 points
#  for a full house. Or you could reroll your 5s and try for
#  the 50-point Yahtzee (which is when all five dice show the
#  same number)  but then youd run the risk of scoring a
# lowly three- or four-of-a-kind instead, which are worth the
#  sum of your five dice.

def getRoll(number):
    """the method returns a tuple of n1, n2 containing two results
    between 1 and 6."""
    n1 = rand.randint(1, 6)
    n2 = rand.randint(1, 6)
    # print((n1, n2))
    return [n1, n2]

def scoreHand(hand):
    """takes a hand and evaluates it, returns a value for the hand"""
    if hand[3] == hand[4]:
        if hand[3] == 4:
            return 50
        return 25
    return sum(hand)

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



# so what do we need?
# a structure to hold 5 die results DONE
# hand = [4, 4, 4]
# a source of random numbers DONE
# a tool to generate results
# a tool to score hands DONE
# graph to show the distribution of interesting quantities


logbook = pd.DataFrame()
rand = random.Random()
rand.seed()
sampleSize = 50000
sample = generateSample(sampleSize)
print(sample['score'].mean())


