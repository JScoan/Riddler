import numpy as np
import pandas as pd
import itertools
import math
import time

def shuffle(shuffleCard, deck):
    slice = deck[:shuffleCard]
    flipped = np.flipud(slice)
    deck[:shuffleCard] = flipped
    return deck

def orderAnalysis(deck):
    counter = 0
    analysis = [0 for i in range(deck.size)]
    while deck[0] != 1:
        counter += 1
        analysis[deck[0]-1] += 1
        deck = shuffle(deck[0], deck)
    return analysis


def shuffler(deck):
    counter = 0
    starting = np.copy(deck)

    while deck[0] != 1:
        counter += 1
        deck = shuffle(deck[0], deck)
    return starting, counter

def pdShuffler(deck):
    counter = 0
    if not (checkShufflePotential(deck)):
        return 0
    elif checkWindability(deck):
        return 0
    else:
        while deck[0] != 1:
            counter += 1
            deck = shuffle(deck[0], deck)
        return counter


def buildDeck(length):
    baseDeck = []
    for num in range(length):
        baseDeck.append(num + 1)
    return baseDeck

def checkWindability(deck):
    # print(deck.size)
    for x in range(deck.size):
        if deck[x] == (x+1):
            if x != 0:
                return True
    return False

def checkShufflePotential(deck):
    marker = deck[0]
    if marker >= deck.size-3:
        return True

    for x in range(marker):
        if (deck[x] > marker):
            return True
    # print(deck)
    return False


def sifter(length):
    base = buildDeck(length)
    # deckList = list(itertools.permutations(base))
    deckListIter = itertools.permutations(base)
    topResult = 0
    topCandidate = []
    # allDecksResults = np.array([])
    while True:
        try:
            nextDeck = deckListIter.next()
            # print(nextDeck)
            candidate, shufflesToFinish = shuffler(np.array(nextDeck))
            if shufflesToFinish >= topResult:
               topCandidate = np.copy(candidate)
               topResult = shufflesToFinish
        except StopIteration:
            break


    # for dlist in deckList:
    #     deckArray = np.array(dlist)
    #     # print(shuffler(deckArray))
    #     allDecksResults = np.append(allDecksResults, shuffler(deckArray))
    return topCandidate, topResult

def pdSifter(length):
    base = buildDeck(length)
    deckListIter = itertools.permutations(base)
    topCandidate = pd.DataFrame()
    sifterSize = 2000000
    first = True
    remainder = math.factorial(length)
    dumpcount = (remainder/length)
    remainder -= dumpcount

    while True:
        try:
            if first:
                print('dumping ' + str(dumpcount) + ' records')
                while dumpcount > sifterSize:
                    dump = (deckListIter.next() for _ in range(sifterSize))
                    # print([x for x in dump])
                    del dump
                    dumpcount -= sifterSize
                    print(str(dumpcount) + ' records to dump')
                remainder += dumpcount



            if remainder > sifterSize:
                gen = (deckListIter.next() for _ in range(sifterSize))
                remainder -= sifterSize
                print(str(remainder) + ' records to search')
            else:
                gen = (deckListIter.next() for _ in range(remainder - 1))
                remainder -= remainder
            innerStart = time.time()
            deckList = [x for x in gen]
            pdList = pd.DataFrame(deckList)
            pdList['result'] = pdList.apply(pdShuffler, axis=1)
            pdListSorted = pdList.sort_values(by=['result'], ascending=False)
            pdListSorted = pdListSorted.reset_index(drop=True)
            innerEnd = time.time()
            print('time per ' + str(sifterSize) + ' records')
            print(innerEnd-innerStart)
            print('ETA: ' + str(remainder * (innerEnd-innerStart)/(3600*sifterSize)))

            if first:
                first = False
                topCandidate = pdListSorted[:1]
                print('first Candidate: ')
                print(topCandidate)

            if topCandidate.loc[0, 'result'] < pdListSorted.loc[0, 'result']:
                topCandidate = pdListSorted[:1]
                print('new Candidate: ')
                print(topCandidate)



        except ValueError:
            break


    return topCandidate

#
# deck = [9, 1, 10, 7, 2, 6, 4, 5, 3, 8, 11]
# # print(shuffler(deck))
run = 13
start = time.time()
result = pdSifter(run)
print('Final:')
print(result)
end = time.time()
# for x in range(7):
#     run = x+2
#     result = pdSifter(run)
analysis = orderAnalysis(result.iloc[0, 0:run])
print(analysis)
print(end - start)
# print([pdSifter(x+1) for x in range(8)])

