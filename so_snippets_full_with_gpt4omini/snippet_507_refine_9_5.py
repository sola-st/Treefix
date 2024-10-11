import operator # pragma: no cover

import operator # pragma: no cover

X = [1, 2, 3, 4, 5] # pragma: no cover
Y = [5, 4, 3, 2, 1] # pragma: no cover
class MockOperator:  # pragma: no cover
    @staticmethod # pragma: no cover
    def itemgetter(index): # pragma: no cover
        return lambda *args: [arg[index] for arg in args] # pragma: no cover
operator = MockOperator() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(2416)

