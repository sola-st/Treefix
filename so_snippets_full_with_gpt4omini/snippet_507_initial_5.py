from operator import itemgetter # pragma: no cover

X = [1, 2, 3, 4] # pragma: no cover
Y = [3, 2, 1, 4] # pragma: no cover
operator = type('Mock', (object,), {'itemgetter': itemgetter})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(2416)

