# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class
from l3.Runtime import _l_
methods = [(func, getattr(o, func)) for func in dir(o) if callable(getattr(o, func))]
_l_(14303)

methods = inspect.getmembers(o, predicate=inspect.ismethod)
_l_(14304)

