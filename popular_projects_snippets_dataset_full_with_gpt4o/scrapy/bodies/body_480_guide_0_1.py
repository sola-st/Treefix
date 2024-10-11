import warnings # pragma: no cover
from types import GeneratorType # pragma: no cover

def is_generator_with_return_value(callable): # pragma: no cover
    if isinstance(callable, GeneratorType): # pragma: no cover
        try: # pragma: no cover
            next(callable) # pragma: no cover
            return hasattr(callable, 'gi_code') and callable.gi_code.co_flags & 0x0020 # pragma: no cover
        except StopIteration: # pragma: no cover
            pass # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
class Spider: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._is_generator = (val for val in range(10)) # pragma: no cover
 # pragma: no cover
    def callable_method(self): # pragma: no cover
        self._is_generator = (val for val in range(10)) # pragma: no cover
        return self._is_generator # pragma: no cover
 # pragma: no cover
spider = Spider() # pragma: no cover
callable = spider.callable_method # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
from l3.Runtime import _l_
"""
    Logs a warning if a callable is a generator function and includes
    a 'return' statement with a value different than None
    """
try:
    _l_(21564)

    if is_generator_with_return_value(callable):
        _l_(21560)

        warnings.warn(
            f'The "{spider.__class__.__name__}.{callable.__name__}" method is '
            'a generator and includes a "return" statement with a value '
            'different than None. This could lead to unexpected behaviour. Please see '
            'https://docs.python.org/3/reference/simple_stmts.html#the-return-statement '
            'for details about the semantics of the "return" statement within generators',
            stacklevel=2,
        )
        _l_(21559)
except IndentationError:
    _l_(21563)

    callable_name = spider.__class__.__name__ + "." + callable.__name__
    _l_(21561)
    warnings.warn(
        f'Unable to determine whether or not "{callable_name}" is a generator with a return value. '
        'This will not prevent your code from working, but it prevents Scrapy from detecting '
        f'potential issues in your implementation of "{callable_name}". Please, report this in the '
        'Scrapy issue tracker (https://github.com/scrapy/scrapy/issues), '
        f'including the code of "{callable_name}"',
        stacklevel=2,
    )
    _l_(21562)
