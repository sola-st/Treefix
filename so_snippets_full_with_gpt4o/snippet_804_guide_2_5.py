import sys # pragma: no cover
import types # pragma: no cover

sys.modules['foo'] = types.ModuleType('foo') # pragma: no cover
sys.modules['foo'].Foo = type('Foo', (object,), {}) # pragma: no cover
def mock_print_classes(): # pragma: no cover
    current_module = sys.modules['foo'] # pragma: no cover
    for key in dir(current_module): # pragma: no cover
        if isinstance(getattr(current_module, key), type): # pragma: no cover
            print(key) # pragma: no cover
sys.modules['foo'].print_classes = mock_print_classes # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
#foo.py
from l3.Runtime import _l_
try:
    import sys
    _l_(14075)

except ImportError:
    pass

class Foo(object):
    _l_(14077)

    pass
    _l_(14076)

def print_classes():
    _l_(14082)

    current_module = sys.modules[__name__]
    _l_(14078)
    for key in dir(current_module):
        _l_(14081)

        if isinstance( getattr(current_module, key), type ):
            _l_(14080)

            print(key)
            _l_(14079)
try:
    import foo
    _l_(14084)

except ImportError:
    pass
foo.print_classes()
_l_(14085)

