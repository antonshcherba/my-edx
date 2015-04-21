__author__ = 'aDmin'

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    sameColorBalls = 0

    for i in range(numTrials):
        bucket = [0,0,0,1,1,1]
        random.shuffle(bucket)

        balls = set()
        for i in range(3):
            choise = random.randint(0, len(bucket)-1)
            balls.add(bucket.pop(choise))

        if (len(balls) == 1):
            sameColorBalls += 1

    return sameColorBalls / float(numTrials)



def main():
    print 'Chances to get balls of the same collor is:', noReplacementSimulation(100000)
    return 0

if __name__ == '__main__':
    main()