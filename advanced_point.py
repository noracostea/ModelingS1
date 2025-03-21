from color_point import ColorPoint

class AdvancedPoint(ColorPoint): # This means we are inheriting from ColorPoint
    COLORS = ["red", "green", "blue", "black", "white"]
    def __init__ (self, x, y, color):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int,float)):
            raise TypeError("y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        # super().__init__(x, y, color) # Call the init method of the parent
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color (self):
        return self._color

    @color.setter
    def color(self, new_color):
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of: {AdvancedPoint.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)**0.5

    @staticmethod
    def from_dictionary(dict):
        x = dict.get("x", 10)
        y = dict.get("y", 20)
        color = dict.get("color", "black")
        return AdvancedPoint(x,y, color)

AdvancedPoint.add_color("amber")
p2 = AdvancedPoint(1,2, "amber")
print(p2.x)
print(p2.y)
p2.color = "blue"
print(p2)
p3 = AdvancedPoint(-1,-2,"blue")
print(AdvancedPoint.distance_2_points(p2, p3))
p4 = AdvancedPoint.from_dictionary({"x": 44})
print(p4)



#print(p2.color)
#p2.color = :"Bob"
#print(p2.color)
#print(p2)

#p = AdvancedPoint(1, 2,"amber")
#print(p)
#print(p.distance_orig())
#p = AdvancedPoint("Jon", "jeb", "blue")
#print(p)
#p.distance_orig()

