__author__ = 'aDmin'

class intDict(object):
    '''A dictionary with integer keys'''

    def __init__(self, numBuckets):
        '''Create an empty dictionary'''
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            