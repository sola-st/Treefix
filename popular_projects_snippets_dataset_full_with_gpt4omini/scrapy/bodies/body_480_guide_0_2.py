import warnings # pragma: no cover
from types import GeneratorType # pragma: no cover

class MockSpider(): # pragma: no cover
    class __class__: # pragma: no cover
        __name__ = 'MockSpider' # pragma: no cover
    @staticmethod # pragma: no cover
    def method(): # pragma: no cover
        yield 'value' # pragma: no cover
        return 'non_none_value' # pragma: no cover
spider = MockSpider() # pragma: no cover
callable = spider.method # pragma: no cover
def is_generator_with_return_value(func): # pragma: no cover
    if isinstance(func(), GeneratorType): # pragma: no cover
        return True if 'return' in func.__code__.co_code else False # pragma: no cover
    return False # pragma: no cover

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
