import numpy as np
import pandas as pd
import itertools
import math
import time


def checkFoldability(deck):
"""this is just a test of local branching"""



def pdSifter(length):
    base = buildDeck(length)
    deckListIter = itertools.permutations(base)
    topCandidate = pd.DataFrame()
    sifterSize = 2000000
    remainder = math.factorial(length)
    dumpcount = (remainder / length)
    remainder -= dumpcount


    print('dumping ' + str(dumpcount) + ' records')
    while dumpcount > sifterSize:
        dump = (deckListIter.next() for _ in range(sifterSize))
        # print([x for x in dump])
        del dump
        dumpcount -= sifterSize
        print(str(dumpcount) + ' records to dump')
    remainder += dumpcount




    # while True:
    #     try:
    #
    #         if remainder > sifterSize:
    #             gen = (deckListIter.next() for _ in range(sifterSize))
    #             remainder -= sifterSize
    #             print(str(remainder) + ' records to search')
    #         else:
    #             gen = (deckListIter.next() for _ in range(remainder - 1))
    #             remainder -= remainder
    #
    #
    #         innerStart = time.time()
    #         deckList = [x for x in gen]
    #         pdList = pd.DataFrame(deckList)
    #         pdList['result'] = pdList.apply(pdShuffler, axis=1)
    #         pdListSorted = pdList.sort_values(by=['result'], ascending=False)
    #         pdListSorted = pdListSorted.reset_index(drop=True)
    #         innerEnd = time.time()
    #         print('time per ' + str(sifterSize) + ' records')
    #         print(innerEnd - innerStart)
    #         print('ETA: ' + str(remainder * (innerEnd - innerStart) / (3600 * sifterSize)))
    #
    #         if first:
    #             first = False
    #             topCandidate = pdListSorted[:1]
    #             print('first Candidate: ')
    #             print(topCandidate)
    #
    #         if topCandidate.loc[0, 'result'] < pdListSorted.loc[0, 'result']:
    #             topCandidate = pdListSorted[:1]
    #             print('new Candidate: ')
    #             print(topCandidate)
    #
    #
    #
    #     except ValueError:
    #         break

    return topCandidate