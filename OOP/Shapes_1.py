"""Shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.__color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.__color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.__color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")
        pass


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        self.__color = super().__init__(color)
        self.__radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.__radius}, color: {self.get_color()})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        self.__circle_area = float(0)
        self.__circle_area = math.pi * self.__radius * self.__radius
        return self.__circle_area


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.color = super().__init__(color)
        self.__side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.__side}, color: {self.get_color()})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        self.__square_area = float(0)
        self.__square_area = self.__side ** 2
        return self.__square_area


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color: str, length: float, width: float):
        """
        Rectangle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.color = super().__init__(color)
        self.__length = length
        self.__width = width

    def __repr__(self) -> str:
        """
        Return representation of the rectangle.

        For this exercise, this should return a string:
        Rectangle (l: {length}, w: {width} color: {color})
        """
        return f"Rectangle (l: {self.__length}, w: {self.__width}, color: {self.get_color()})"

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Area of the rectangle is length * width.
        """
        self.__rectangle_area = float(0)
        self.__rectangle_area = self.__length * self.__width
        return self.__rectangle_area


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.__shapes = []

    def add_shape(self, shape: Shape):
        """Add a shape to the program."""
        self.__shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.__shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0
        for shape in self.__shapes:
            total_area += float(shape.get_area())
        return total_area

    def get_circles(self) -> list:
        """Return only circles."""
        circle = []
        for shape in self.__shapes:
            if isinstance(shape, Circle):
                circle.append(shape)
        return circle

    def get_squares(self) -> list:
        """Return only squares."""
        qsuare = []
        for shape in self.__shapes:
            if isinstance(shape, Square):
                square.append(shape)
        return square

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangle = []
        for shape in self.__shapes:
            if isinstance(shape, Rectangle):
                rectangle.append(shape)
        return rectangle


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    rectangle = Rectangle("green", 12, 8)
    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)
    print(paint.calculate_total_area())
    print(paint.get_circles())