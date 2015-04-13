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