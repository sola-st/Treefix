# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
#foo.py
from l3.Runtime import _l_
try:
    import sys
    _l_(1899)

except ImportError:
    pass

class Foo(object):
    _l_(1901)

    pass
    _l_(1900)

def print_classes():
    _l_(1906)

    current_module = sys.modules[__name__]
    _l_(1902)
    for key in dir(current_module):
        _l_(1905)

        if isinstance( getattr(current_module, key), type ):
            _l_(1904)

            print(key)
            _l_(1903)
try:
    import foo
    _l_(1908)

except ImportError:
    pass
foo.print_classes()
_l_(1909)

