__author__ = 'aDmin'

import DrunkenWalk
import random
import pylab

def walk(f, d, numSteps):
    start = f.getLoc(d)

    for step in range(numSteps):
        f.moveDrunk(d)
    return (start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials, dClass=DrunkenWalk.UsualDrunk):
    homer = dClass('Homer')
    origin = DrunkenWalk.Location(0, 0)
    distances = []

    for trial in range(numTrials):
        f = DrunkenWalk.Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials):
    random.seed(0)
    for numSteps in [10, 100, 1000, 10000, 100000]:
    # for numSteps in [0,1]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print 'Mean = ', sum(distances)/len(distances)
        print 'Max = ', max(distances), ' Min = ', min(distances)

#drunkTest(20)

def drunkTestPlot(numTrials=50):
    stepsTaken = [10, 100, 1000, 10000, 100000]
    for dClass in (DrunkenWalk.UsualDrunk, DrunkenWalk.ColdDrunk, DrunkenWalk.EDrunk):
        meanDistances = []
        #squareRoot = []

        for numSteps in stepsTaken:
            distances = simWalks(numSteps,numTrials)
            meanDistances.append(sum(distances)/len(distances))
            #squareRoot.append(numSteps ** 0.5)

        pylab.plot(stepsTaken, meanDistances, label=dClass.__name__)
    #pylab.plot(stepsTaken, squareRoot, label='Square root of steps')
    pylab.title('Mean distance from Origin')
    pylab.xlabel('Steps taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend(bbox_to_anchor=(0.5, 1.05))
    pylab.show()

drunkTestPlot()