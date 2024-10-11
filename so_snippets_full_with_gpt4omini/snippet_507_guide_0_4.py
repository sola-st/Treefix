import operator # pragma: no cover

X = [3, 1, 4, 1, 5, 9] # pragma: no cover
Y = [2, 7, 1, 8, 2, 8] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(2416)

