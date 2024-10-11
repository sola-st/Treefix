import operator # pragma: no cover

X = [3, 1, 2] # pragma: no cover
Y = [4, 5, 6] # pragma: no cover
operator.itemgetter = lambda i: lambda x: x[i] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(14777)

