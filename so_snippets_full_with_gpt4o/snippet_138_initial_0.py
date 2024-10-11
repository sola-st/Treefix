from pprint import pprint # pragma: no cover

class YourObject:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.attribute1 = 'value1'# pragma: no cover
        self.attribute2 = 42# pragma: no cover
        self.attribute3 = [1, 2, 3]# pragma: no cover
your_object = YourObject() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
from l3.Runtime import _l_
try:
    from pprint import pprint
    _l_(14312)

except ImportError:
    pass
pprint(vars(your_object))
_l_(14313)

