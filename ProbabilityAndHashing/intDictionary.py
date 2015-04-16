__author__ = 'aDmin'

class intDict(object):
    '''A dictionary with integer keys'''

    def __init__(self, numBuckets):
        '''Create an empty dictionary'''
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, dictKey, dictVal):
        '''Assumes dictKey an int. Adds an entry'''
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if (hashBucket[i][0] == dictKey):
                hashBucket[i] = (dictKey,dictVal)
                return
        hashBucket.append((dictKey,dictVal))

    def getValue(self, dictKey):
        '''Assumes dictKey is an int. Returns entry associated with the dictKey'''
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None

    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}'

def collision_prob(numBuckets, numInsertions):
    '''
    Given the number of buckets and the number of items to insert,
    calculates the probability of a collision.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numBuckets - i) / float(numBuckets))
    return 1 - prob

def sim_insertions(numBuckets, numInsertions):
    '''
    Run a simulation for numInsertions insertions into the hash table.
    '''
    choices = range(numBuckets)
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return False
        else:
            used.append(hashVal)
    return True

def observe_prob(numBuckets, numInsertions, numTrials):
    '''
    Given the number of buckets and the number of items to insert,
    runs a simulation numTrials times to observe the probability of a collision.
    '''
    probs = []
    for t in range(numTrials):
        probs.append(sim_insertions(numBuckets, numInsertions))
    return 1 - sum(probs)/float(numTrials)

import random

def numBucketsSearch():
    numBuckets = 365
    numInsertionsMax = 365
    numInsertionsMin = 0
    repeatCount = 0
    while (True):
        avg = (numInsertionsMax - numInsertionsMin) / 2 + numInsertionsMin
        repeatCount +=1
        if (collision_prob(numBuckets, avg) < 0.99
            and collision_prob(numBuckets,avg) > 0.98):
            print 'count =', repeatCount
            return avg
        elif (collision_prob(numBuckets, avg) < 0.99):
            numInsertionsMin = avg
        elif (collision_prob(numBuckets, avg) > 0.99):
            numInsertionsMax = avg



def main():
    # D = intDict(29)
    # for i in range(20):
    #     key = random.choice(range(10**5))
    #     D.addEntry(key,i)
    #
    # print '\n', 'The buckets are:'
    # for hashBucket in D.buckets:
    #     print ' ', hashBucket


    # print 'Colision probability of ', str(50),\
    #     ' insertions to ', str(1000),\
    #     ' buckets is ',collision_prob(numBuckets=1000, numInsertions=50)
    # print 'Colision probability of ', str(200),\
    #     ' insertions to ', str(1000),\
    #     ' buckets is ',collision_prob(numBuckets=1000, numInsertions=200)
    #
    # print 'Simulation of ', str(50),\
    #     ' insertions to ', str(1000),\
    #     ' buckets is ',observe_prob(numBuckets=1000, numInsertions=50,
    #                                 numTrials=1000)
    # print 'Simulation of ', str(200),\
    #     ' insertions to ', str(1000),\
    #     ' buckets is ',observe_prob(numBuckets=1000, numInsertions=200,
    #                                 numTrials=1000)
    #
    # print 'Simulation of ', str(30),\
    #     ' insertions to ', str(365),\
    #     ' buckets is ',collision_prob(numBuckets=365, numInsertions=30)
    # print 'Simulation of ', str(250),\
    #     ' insertions to ', str(365),\
    #     ' buckets is ',observe_prob(numBuckets=365, numInsertions=250,
    #                                 numTrials=1000)
    
    print numBucketsSearch()


if __name__ == '__main__':
    main()