import inspect # pragma: no cover

func = type('MockFunction', (object,), {'__call__': lambda self: None, 'method': lambda self, val, flags=0: None})() # pragma: no cover

import inspect # pragma: no cover

def test_function(pattern, string, flags=0): # pragma: no cover
    pass # pragma: no cover
func = test_function # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
from l3.Runtime import _l_
"""Returns (args, kwargs) tuple for a function
    >>> import re
    >>> get_spec(re.match)
    (['pattern', 'string'], {'flags': 0})

    >>> class Test:
    ...     def __call__(self, val):
    ...         pass
    ...     def method(self, val, flags=0):
    ...         pass

    >>> get_spec(Test)
    (['self', 'val'], {})

    >>> get_spec(Test.method)
    (['self', 'val'], {'flags': 0})

    >>> get_spec(Test().method)
    (['self', 'val'], {'flags': 0})
    """

if inspect.isfunction(func) or inspect.ismethod(func):
    _l_(20924)

    spec = inspect.getfullargspec(func)
    _l_(20920)
elif hasattr(func, '__call__'):
    _l_(20923)

    spec = inspect.getfullargspec(func.__call__)
    _l_(20921)
else:
    raise TypeError(f'{type(func)} is not callable')
    _l_(20922)

defaults = spec.defaults or []
_l_(20925)

firstdefault = len(spec.args) - len(defaults)
_l_(20926)
args = spec.args[:firstdefault]
_l_(20927)
kwargs = dict(zip(spec.args[firstdefault:], defaults))
_l_(20928)
aux = (args, kwargs)
_l_(20929)
exit(aux)
