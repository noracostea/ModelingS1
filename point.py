import random
class Point:
    """
    Class modeling a real life 20 point
    """
    def __init__(self,x,y):
        """
        Initialize the point instance
        :param x: the x-axis coordinate value
        :param y: the y-axis coordinate value
        """
        self.x=x
        self.y=y

    def __str__(self):
        """
        Magic method that defines how a point is printed
        """
        return f"<{self.x},{self.y}>"

    def __repr__(self):
        """
        Magic method that defines the string representation of an object
        :return:the point as a string
        """
        return self.__str__()

    def distance_orig(self):
        """
        Regular method that finds the distance form the point to the origin
        :return: distance
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self,other): #"greater than" compares the points
        """
        Magic method that is called when you do self>other
        :param other: the other point comparing against
        :return: True/False
        """
        return self.distance_orig() > other.distance_orig()

    def __eq__(self,other):
        """
        Magic method that finds if a point is equal to another based on their distance to the origin
        :param other: another point
        :return:True/false
        """
        return self.distance_orig() == other.distance_orig()


#By not indenting this is no longer in the class

p1=Point(1,2) #create a new instance of the class
p2=Point(3,4)
p3=Point("James", "Jane") #valid but probably not intended
print(p1.x,p1.y) #access attributes, attributes of class are x and y
print(p1)

if __name__=="__main__":
    points=[]
    for i in range(5):
        #create a random point
        p=Point(
            random.randint(-100,100),
            random.randint(-100,100)
        )
        #append it to the list
        points.append(p)
    for point in points:
        print(points)

    #points.sort
    p=Point(-12,-5)
    print(p.distance_orig())

    p1=(4,6)
    p2=(7,7)

    print(p1.__gt__(p2))
    print("unsorted points")
    print(points)
    print("sorted points")
    points.sort()
    print(points)

    found_equal=0
    count=0
    while True:
        if found_equal==10:
            break
        p1=Point(random.randint(-100,100),
            random.randint(-100,100))
        p2=Point(random.randint(-100,100),
            random.randint(-100,100))
        count+=1
        if p1==p2:
            print(p1,p2)
            found_equal+=1
    print(f"Probability is 1 in {count/found_equal}")