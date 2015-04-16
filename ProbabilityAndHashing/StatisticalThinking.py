__author__ = 'aDmin'

import random
import pylab

def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    N = len(L)
    allLen = 0.0
    if (len(L) == 0):
        return float('NaN')

    for str in L:
        allLen += len(str)

    mean = allLen / N
    s = 0.0
    for str in L:
        s += (len(str) - mean) ** 2

    return (s / N) ** 0.5

def flipPlot(minExp, maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)

    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))

    pylab.title('Difference between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(Heads - Tails)')
    pylab.plot(xAxis,diffs, 'o')

    pylab.figure()
    pylab.title('Heads/Tails ratio')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis,ratios)

def main():
    # print 'Standard deviation of [a, z, p] is',\
    #     str(stdDevOfLengths(['a', 'z', 'p']))
    # print 'Standard deviation of [apples, oranges, kiwis, pineapples] is',\
    #     str(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))

    random.seed(2)
    flipPlot(4, 20)
    pylab.show()

if __name__ == '__main__':
    main()

