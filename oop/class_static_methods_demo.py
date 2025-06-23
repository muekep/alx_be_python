class Calculator:
    """
    A simple Calculator class demonstrating class methods and static methods.
    """

    # Class Attribute: Accessible via the class itself or instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method that returns the sum of two numbers.
        It does not access or modify class-specific or instance-specific data.
        """
        print(f"Performing static addition: {a} + {b}")
        return a + b

    @classmethod
    def multiply(cls, a, b) -> float:
        """
        A class method that returns the product of two numbers.
        It has access to the class itself (via 'cls' parameter) and its attributes.
        """
        # Accessing the class attribute using 'cls'
        print(f"Calculation Type: {cls.calculation_type}")
        print(f"Performing class method multiplication: {a} * {b}")
        return a * b
