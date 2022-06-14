import random
import math

# Creates Point class
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Creates distance_to_origine method for calculating distance to origine of a point object
    def distance_to_origine(self):
        self.distance=math.sqrt(self.x**2+self.y**2)
        return self.distance
    
# Function that generates objects of the Point class in an amount defined by user by using random library.   
def generateListOfPoints ():
    # Creates empty list in which points will be stored
    list=[]
    # The user is prompted to define the number of points.
    numberOfPoints = int(input("Please, define the number of points to create:"))
    for i in range(numberOfPoints):
        point.x = random.randint(-100,100)
        point.y = random.randint(-100,100)
        print(point.x, point.y, point.distance_to_origine(point))
        list.append(point)
    for j in range(numberOfPoints):
        print(list[j].x, list[j].y, list[j].distance_to_origine(list[j]))
    return list

# Test function
def main():
    generateListOfPoints ()

if __name__ == "__main__":
    main()
