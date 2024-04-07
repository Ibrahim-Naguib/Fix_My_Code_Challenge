#!/usr/bin/python3

class square():
    """
    A class representing a square shape.

    Attributes:
    - width: The width of the square.
    - height: The height of the square.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a square with the given width and height.
        
        Args:
        - width: The width of the square.
        - height: The height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
