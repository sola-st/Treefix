import operator # pragma: no cover

X = [1, 3, 2, 4] # pragma: no cover
Y = [40, 10, 20, 30] # pragma: no cover
operator = type('Mock', (object,), {'itemgetter': operator.itemgetter}) # pragma: no cover

import operator # pragma: no cover

X = [4, 1, 3, 2] # pragma: no cover
Y = [40, 10, 30, 20] # pragma: no cover
operator = type('Mock', (object,), {'itemgetter': operator.itemgetter}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(14777)

