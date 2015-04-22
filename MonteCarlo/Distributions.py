__author__ = 'aDmin'

import random
import pylab

def makeNormal(mean, sd, numSamples):
    samples = []
    for i in range(numSamples):
        samples.append(random.gauss(mean,sd))

    pylab.hist(samples,bins=101)

def main():
    makeNormal(4, 8, 100000)
    pylab.show()
    return 0

if __name__ == '__main__':
    main()