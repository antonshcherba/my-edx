__author__ = 'aDmin'

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

def main():
    print 'Standard deviation of [a, z, p] is',\
        str(stdDevOfLengths(['a', 'z', 'p']))
    print 'Standard deviation of [apples, oranges, kiwis, pineapples] is',\
        str(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))

if __name__ == '__main__':
    main()

