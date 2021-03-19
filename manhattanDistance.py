#Author: Michael Schoenleb
#Date: 3/17
#Purpose: Ford Software Programming Assessment, a program that accepts the x and y coordinates of two points ona  grid, and then calculates the manhattan distance between them.

#manhattan distance calculation function: |x1-x2|+|y1-y2|
def manhattanDistance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    
    
# test class to run some internal test cases
class distanceTest():
    def __init__(self):
        if self.distanceTest1() and self.distanceTest2() and self.distanceTest3() and self.distanceTest4() and self.distanceTest5():
            print("Internal test cases passed")
    def distanceTest1(self):
        return manhattanDistance([5,4],[3,2]) == 4
    def distanceTest2(self):
        return manhattanDistance([-1,2],[1,-2]) == 6
    def distanceTest3(self):
        return manhattanDistance([1,2],[1,2]) == 0
    def distanceTest4(self):
        return manhattanDistance([-1,-2],[-2,-1]) == 2
    def distanceTest5(self):
        return manhattanDistance([0,0],[0,0]) == 0



distanceTest()

# user input section. The split allows a multiple part user input on one line
x1,y1 = input("Enter the integer X and Y values for the FIRST point seperated by a space: ").split()
x2,y2 = input("Enter the integer X and Y values for the SECOND point seperated by a space: ").split()

#convert str to int then combine the user input coordinates into two lists to be input into the function
#point 1
p1 = [int(x1), int(y1)]
#point 2
p2 = [int(x2), int(y2)]

#output the result
print("Manhattan Distance: "+ str(manhattanDistance(p1,p2)))