

class Elevator():

    def __init__(self, lowestFloor, highestFloor, currentFloor):
        """
        For this exercise, this elevator will be using the North 
        American convention of building stories. This convention
        has the floor 1 as the lobby, floor 0 as the lowest
        lobby and any floor below that is a negative number.
        """
        self.lowestFloor = lowestFloor
        self.highestFloor = highestFloor
        self.currentFloor = currentFloor

    def goUp(self, numberOfFloors):
        intendedFloor = self.currentFloor + numberOfFloors
        if intendedFloor > self.highestFloor:
            print "This building only has {} floors. Try again".format(
                self.highestFloor)
        else:
            self.currentFloor += numberOfFloors
            print "Heading to floor #{}".format(self.currentFloor)

    def goDown(self, numberOfFloors):
        intendedFloor = self.currentFloor + numberOfFloors
        if intendedFloor < self.lowestFloor:
            print "This building's lowest floor is {}. Try again".format(
                self.lowestFloor)
        else:
            self.currentFloor -= numberOfFloors
            print "Heading to floor #{}".format(self.currentFloor)

    def goToFloor(self, floorNumber):
        if self.lowestFloor > floorNumber < self.highestFloor:
            self.currentFloor = floorNumber
        else:
            print "Not a valid floor number. Please try again"

