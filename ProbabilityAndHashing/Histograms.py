__author__ = 'aDmin'

import random
import pylab

def stdDev(data):
    mean = sum(data)/float(len(data))
    tot = 0.0
    for val in data:
        tot += (val - mean)**2

    return (tot / len(data))**0.5

def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1.0

    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads,mean,sd)


