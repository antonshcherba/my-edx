__author__ = 'aDmin'

import DrunkenWalk

def walk(f, d, numSteps):
    start = f.getLoc(d)

    for step in range(numSteps):
        f.moveDrunk(d)
    return (start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = DrunkenWalk.UsualDrunk('Homer')
    origin = DrunkenWalk.Location(0, 0)
    distances = []

    for trial in range(numTrials):
        f = DrunkenWalk.Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numTrials))
    return distances

def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 10000, 100000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print 'Mean = ', sum(distances)/len(distances)
        print 'Max = ', max(distances), ' Min = ', min(distances)

drunkTest(100)