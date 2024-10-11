import inspect # pragma: no cover
import re # pragma: no cover

import inspect # pragma: no cover
import re # pragma: no cover

func = re.match # pragma: no cover
inspect = type('MockInspect', (object,), {'isfunction': staticmethod(lambda f: callable(f)), 'ismethod': staticmethod(lambda m: callable(m)), 'getfullargspec': staticmethod(lambda f: inspect.FullArgSpec(args=['pattern', 'string'], varargs=None, varkw=None, defaults=(0,), keywordonlyargs=[], keywordonlydefaults=None, annotations={})), 'signature': staticmethod(lambda f: type('MockSignature', (object,), {'parameters': {'pattern': 'Parameter', 'string': 'Parameter'}}))})() # pragma: no cover

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
    _l_(9720)

    spec = inspect.getfullargspec(func)
    _l_(9716)
elif hasattr(func, '__call__'):
    _l_(9719)

    spec = inspect.getfullargspec(func.__call__)
    _l_(9717)
else:
    raise TypeError(f'{type(func)} is not callable')
    _l_(9718)

defaults = spec.defaults or []
_l_(9721)

firstdefault = len(spec.args) - len(defaults)
_l_(9722)
args = spec.args[:firstdefault]
_l_(9723)
kwargs = dict(zip(spec.args[firstdefault:], defaults))
_l_(9724)
aux = (args, kwargs)
_l_(9725)
exit(aux)
