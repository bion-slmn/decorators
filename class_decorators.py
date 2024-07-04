from typing import Any, Callable, List


class MyDecorator:
    """
    A decorator that stores and processes function results.

    This decorator stores function results in memory
    and provides methods to retrieve the memory,
    find the biggest value, and find the smallest value.

    Args:
        func: The function to be decorated.

    Returns:
        The result of the decorated function.

    Raises:
        ValueError: If any argument passed to the decorated
        function is not an integer.
    """

    def __init__(self, func: Callable[..., Any]) -> None:
        self._func = func
        self._memory: List[Any] = []
        self._funcargs: List[int] = []

    def memory(self) -> List[Any]:
        """Returns the memory of stored function results."""
        return self._memory

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Calls the decorated function with 
        validation and stores the result."""
        if not all(isinstance(arg, int) for arg in args):
            raise ValueError('Numbers only')
        self._funcargs = list(args)
        result = self._func(*args, **kwds)
        self._memory.append(result)
        print('The result is', result)
        return result

    def biggest_value(self) -> int:
        """Returns the biggest value from the last function arguments."""
        if self._funcargs:
            maxim = max(self._funcargs)
            print("The maximum value is:", maxim)
            return maxim
        raise ValueError("No arguments provided to the function.")

    def smallest_value(self) -> int:
        """Returns the smallest value from the last function arguments."""
        if self._funcargs:
            minim = min(self._funcargs)
            print("The minimum value is:", minim)
            return minim
        raise ValueError("No arguments provided to the function.")


@MyDecorator
def sum_numbers(*args: int) -> int:
    """Returns the sum of the provided arguments."""
    return sum(args)


# Example Usage
try:
    sum_numbers(1, 3, 4, 4)
    sum_numbers.biggest_value()
    sum_numbers.smallest_value()
    sum_numbers(1, 3, 4, 'b', 22, 39)
except ValueError as e:
    print(e)

print(sum_numbers.memory())
