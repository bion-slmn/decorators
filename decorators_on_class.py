'''
This module defines a decorator that can be use on a class
I wrapps all methods  of the class with an exception
'''
from functools import wraps


def handle_exception(func):
    """
    Wraps a function to handle exceptions gracefully.

    Args:
        func: The function to be wrapped.

    Returns:
        The result of the function if successful, otherwise an error message.
    """
    @wraps(func)
    def wrapper(*args):
        try:
            func(*args)
        except Exception as e:
            return f"Error: {e}"
    return wrapper


def method_exception_handler(cls):
    """
    Handles exceptions for all methods in a class by
    wrapping them with an exception handler.

    Args:
        cls: The class to decorate its methods with exception handling.

    Returns:
        The class with all its methods wrapped with exception handling.
    """

    for name, value in vars(cls).items():
        if callable(value):
            setattr(cls, name, handle_exception(value))
    return cls


@method_exception_handler
class Mathematics:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multi(self):
        return self.a * self.b

    def sub(self):
        if self.a < 0:
            raise ValueError('A must be greater than 0')
        return self.a - self.b


math = Mathematics(-1, 3)

print(math.sub())
