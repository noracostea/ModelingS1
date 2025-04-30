from color_point import ColorPoint

class AdvancedPoint(ColorPoint): #means we are inheriting from ColorPoint
    COLORS=["red","green","blue","black","white"]
    def __init__(self,x,y,color):
        """
        Magic method to initialize an advanced point with validation for coordinates and color.
        :param x: x value
        :param y: y value
        :param color: color of point
        """
        if not isinstance(x,(int,float)):
            raise TypeError("x must be a number")
        if not isinstance(y,(int,float)):
            raise TypeError("y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        #super().__init__(x,y,color) #call the init method of the parent
        self._x=x
        self._y=y
        self._color=color

    @property
    def x(self):#"hides" x from the user
        """
        Gets x-coordinate value as an attribute instead of a method
        :return: x-coordinate value as int/float
        """
        return self._x

    @property
    def y(self):
        """
        Gets y-coordinate value as an attribute instead of a method
        :return: y-coordinate value as int/float
        """
        return self._y

    @property
    def color(self):
        """
        Gets point's color
        :return:current color of point as str
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Sets a new color for the point with validation
        :param new_color:new color to assign to point
        :return:point with new color
        """
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of: {AdvancedPoint.COLORS}")
        self._color=new_color

    @classmethod
    def add_color(cls,new_color):
        """
        Adds new color to the class' available COLORS list
        :param new_color:new color to add to list
        :return:list appended
        """
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1,p2): #no reference to class or self
        """
        Calculates distance between two points
        :param p1:point 1
        :param p2:point 2
        :return: distance between point 1 and point 2
        """
        return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5

    @staticmethod
    def from_dictionary(dict):
        """
        Creates an advanced point from a dictionary, point "factory"
        :param dict: dictionary containing x,y and color keys
        :return:advanced point
        """
        x= dict.get("x",10) #second element is default if cant find first element in dict
        y= dict.get("y",20)
        color=dict.get("color","black")
        return AdvancedPoint(x,y,color)

AdvancedPoint.add_color("amber")
p2=AdvancedPoint(1,2,"amber")
print(p2)
print(p2.color)
print(p2.color)
print(p2)
print(p2.x)
print(p2.y)
p2.color="blue"
print(p2)


p3=AdvancedPoint(-1,-2,"blue")
print(AdvancedPoint.distance_2_points(p2,p3))

p4=AdvancedPoint.from_dictionary({}) #prints default
print(p4)
p5=AdvancedPoint.from_dictionary({"x":44})
print(p5)
