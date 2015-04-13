__author__ = 'aDmin'

import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result += str(rollDie())

    return result

def getTarget(goal):
    ''' Rolls one dice len(goal) times to know
    how many times it matches the goal
    :param goal: user suggested  values of dices
    :return: number of tries that got the goal
    '''
    numTries = 0
    numRolls = len(goal)
    while (True):
        numTries +=1
        result = rollN(numRolls)
        if (result == goal):
            return numTries

if __name__ == '__main__':
    main()