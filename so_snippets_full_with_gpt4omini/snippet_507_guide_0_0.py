import operator # pragma: no cover
from typing import List, Tuple # pragma: no cover

X: List[int] = [3, 1, 4, 1, 5] # pragma: no cover
Y: List[int] = [9, 2, 6, 5, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
from l3.Runtime import _l_
zip(*sorted(zip(X,Y), key=operator.itemgetter(1)))[0]
_l_(2416)

