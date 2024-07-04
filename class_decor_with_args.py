from typing import Any
from typing import Any, Callable, List, Optional


class Power:
    """
    A decorator class that raises the result of a
    function to a power specified during initialization.

    Args:
        args: The power to raise the result to.

    Returns:
        A wrapped function that raises the result to the specified power.
    """

    def __init__(self, args) -> None:
        self._args = args

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(a, b):
            result = func(a, b)
            return result ** self._args
        return wrapper


@Power(2)
def multipy(a, b):
    return a * b


print(multipy(2, 2))
