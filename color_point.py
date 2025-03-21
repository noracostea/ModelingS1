from point import Point # point is the file, Point is the class

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Defines a color point x, y, color
        :param x:
        :param y:
        :param color:
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.x},{self.y}>({self.color})"

if __name__ == '__main__': #To make nsure that the code does not run when import
    color_points = []
    colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
    for _ in range(5):
        p = ColorPoint(
            random.randint(-100,100),
            random.randint(-100,100),
            random.choice(colors))
        color_points.append(p)
    print("random color points:")
    print(color_points)
    color_points.sort()
    print("color points in order:")
    print(color.points)

