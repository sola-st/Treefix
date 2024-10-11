import inspect # pragma: no cover

class Mock: pass # pragma: no cover
o = Mock() # pragma: no cover
o.method1 = lambda: 'method1' # pragma: no cover
o.method2 = lambda: 'method2' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class
from l3.Runtime import _l_
methods = [(func, getattr(o, func)) for func in dir(o) if callable(getattr(o, func))]
_l_(2532)

methods = inspect.getmembers(o, predicate=inspect.ismethod)
_l_(2533)

