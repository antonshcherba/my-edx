__author__ = 'aDmin'

import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result += str(rollDie())

    return result

if __name__ == '__main__':
    main()