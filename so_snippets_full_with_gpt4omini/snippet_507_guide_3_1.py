import operator # pragma: no cover

X = [10, 30, 20, 40] # pragma: no cover
Y = [3, 1, 2, 4] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(2416)

