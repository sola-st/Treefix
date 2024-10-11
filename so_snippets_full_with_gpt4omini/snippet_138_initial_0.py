from pprint import pprint # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.attr1 = 'value1'# pragma: no cover
        self.attr2 = 42# pragma: no cover
    def method1(self):# pragma: no cover
        return 'method result'# pragma: no cover
    def method2(self, param):# pragma: no cover
        return param * 2# pragma: no cover
# pragma: no cover
your_object = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
from l3.Runtime import _l_
try:
    from pprint import pprint
    _l_(2128)

except ImportError:
    pass
pprint(vars(your_object))
_l_(2129)

