# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.cleanedTiles = []
        # raise NotImplementedError

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # raise NotImplementedError
        x = pos.getX()
        y = pos.getY()
        if not (isinstance(x, float)):
            x = float(x)
        if not (isinstance(y, float)):
            y = float(y)

        tileX = int(math.floor(x))
        tileY = int(math.floor(y))
        for tile in self.cleanedTiles:
            if (tile.getX() == tileX and
                tile.getY() == tileY):
                return
        self.cleanedTiles.append(Position(tileX,tileY))

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # raise NotImplementedError
        for tile in self.cleanedTiles:
            if (tile.getX() == m and tile.getY() == n):
                return True

        return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # raise NotImplementedError
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # raise NotImplementedError
        return len(self.cleanedTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # raise NotImplementedError
        randomX = random.uniform(0,self.width)
        randomY = random.uniform(0,self.height)
        return Position(randomX, randomY)


    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # raise NotImplementedError
        if (pos.getX() >= 0 and pos.getX() < self.width and
            pos.getY() >= 0 and pos.getY() < self.height):
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # raise NotImplementedError
        self.speed = speed
        self.position = room.getRandomPosition()
        room.cleanTileAtPosition(self.position)
        self.direction = random.randint(0,360)
        self.room = room

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # raise NotImplementedError
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # raise NotImplementedError
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # raise NotImplementedError
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # raise NotImplementedError
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # raise NotImplementedError
        while (True):
            newPosition = self.position.getNewPosition(self.direction,
                                                       self.speed)
            if (self.room.isPositionInRoom(newPosition)):
                self.position = newPosition
                self.room.cleanTileAtPosition(newPosition)
                break
            else:
                self.direction = random.randint(0,360)


# Uncomment this line to see your implementation of StandardRobot in action!
##testRobotMovement(StandardRobot, RectangularRoom)

# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    steps = []
    for trial in range(0, num_trials):
        room = RectangularRoom(width,height)
        robots = []
        step = 0
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height, 1.0)
        for i in range(0, num_robots):
            robots.append(robot_type(room,speed))

        while (True):
            #anim.update(room, robots)
            for robot in robots:
                frac = room.getNumCleanedTiles() / float(room.getNumTiles())
                if (frac >= min_coverage):
                    break
                robot.updatePositionAndClean()
                step +=1


            if (room.getNumCleanedTiles() / float(room.getNumTiles()) >= min_coverage):
                    step = math.ceil(step / float(num_robots))
                    steps.append(step)
                    break

        #anim.done()

    return sum(steps) / float(len(steps))

# Uncomment this line to see how much your simulation takes on average
print  runSimulation(1, 1.0, 10, 10, 0.78, 10,StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while (True):
            self.direction = random.randint(0,360)
            newPosition = self.position.getNewPosition(self.direction,
                                                       self.speed)
            if (self.room.isPositionInRoom(newPosition)):
                self.position = newPosition
                self.room.cleanTileAtPosition(newPosition)
                break
        #raise NotImplementedError

print  runSimulation(1, 1.0, 10, 10, 0.78, 10,RandomWalkRobot)




def main():
    # room = RectangularRoom(10, 8)
    # print 'Cleaned tiles in room', str(room.getNumCleanedTiles())
    # print 'Total number of tiles', str(room.getNumTiles())
    # routerPos = room.getRandomPosition()
    # print 'Router position is', str(routerPos)
    # room.cleanTileAtPosition(routerPos)
    # room.cleanTileAtPosition(Position(1,1))
    # print 'Cleaned tiles in room', str(room.getNumCleanedTiles())
    # if room.isPositionInRoom(routerPos):
    #     print 'Router is in the room'
    #
    # room.cleanTileAtPosition(Position(0.6, 0.3))
    # room.cleanTileAtPosition(Position(0.8, 0.8))
    # room.cleanTileAtPosition(Position(0.2, 0.5))
    # print 'Cleaned tiles in room', str(room.getNumCleanedTiles())

    showPlot1('aaa', 'bbb', 'ccc')
    return 0


if __name__ == '__main__':
    main()

