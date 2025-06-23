import math

class Shape:
    """
    Base class for geometric shapes.
    Defines an area() method that must be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method must be overridden by concrete derived classes.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Calculates its area based on length and width.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Overrides the base class area() method to calculate the rectangle's area.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Calculates its area based on its radius.
    """
    def __init__(self, radius: float):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        self.radius = radius

    def area(self) -> float:
        """
        Overrides the base class area() method to calculate the circle's area.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def __str__(self):
        """
        Returns a string representation of the Circle object.
        """
        return f"Circle(Radius: {self.radius})"
