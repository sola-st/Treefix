import inspect # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
from l3.Runtime import _l_
try:
    import inspect
    _l_(1431)

except ImportError:
    pass
method_names = [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]
_l_(1432)
try:
    import inspect
    _l_(1434)

except ImportError:
    pass
methods = [member for member in [getattr(self, attr) for attr in dir(self)] if inspect.ismethod(member)]
_l_(1435)

