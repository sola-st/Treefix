import warnings # pragma: no cover
from typing import Callable, Generator # pragma: no cover

def is_generator_with_return_value(func: Callable) -> bool:# pragma: no cover
    return (isinstance(func, Generator)) and any('return' in line for line in func.__code__.co_code) # pragma: no cover
spider = type('MockSpider', (), {})()  # Creating a mock spider object # pragma: no cover
spider.__class__.__name__ = 'MockSpiderClass'  # Assigning a name to the mock class # pragma: no cover
def mock_callable():# pragma: no cover
    yield 1# pragma: no cover
    return 2  # A generator function with a return value other than None # pragma: no cover
callable = mock_callable # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
from l3.Runtime import _l_
"""
    Logs a warning if a callable is a generator function and includes
    a 'return' statement with a value different than None
    """
try:
    _l_(10246)

    if is_generator_with_return_value(callable):
        _l_(10242)

        warnings.warn(
            f'The "{spider.__class__.__name__}.{callable.__name__}" method is '
            'a generator and includes a "return" statement with a value '
            'different than None. This could lead to unexpected behaviour. Please see '
            'https://docs.python.org/3/reference/simple_stmts.html#the-return-statement '
            'for details about the semantics of the "return" statement within generators',
            stacklevel=2,
        )
        _l_(10241)
except IndentationError:
    _l_(10245)

    callable_name = spider.__class__.__name__ + "." + callable.__name__
    _l_(10243)
    warnings.warn(
        f'Unable to determine whether or not "{callable_name}" is a generator with a return value. '
        'This will not prevent your code from working, but it prevents Scrapy from detecting '
        f'potential issues in your implementation of "{callable_name}". Please, report this in the '
        'Scrapy issue tracker (https://github.com/scrapy/scrapy/issues), '
        f'including the code of "{callable_name}"',
        stacklevel=2,
    )
    _l_(10244)
