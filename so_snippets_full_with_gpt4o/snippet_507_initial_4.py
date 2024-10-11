import operator # pragma: no cover

X = [3, 1, 4, 2] # pragma: no cover
Y = [9, 8, 7, 6] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(14777)

