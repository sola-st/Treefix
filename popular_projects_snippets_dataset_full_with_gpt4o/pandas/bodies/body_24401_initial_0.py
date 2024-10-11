from pandas import Series # pragma: no cover

body = ['text1', 'text2longer', 'short', 'longesttext'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/html.py
from l3.Runtime import _l_
data = [len(elem) for elem in body]
_l_(20879)
lens = Series(data)
_l_(20880)
lens_max = lens.max()
_l_(20881)
not_max = lens[lens != lens_max]
_l_(20882)

empty = [""]
_l_(20883)
for ind, length in not_max.items():
    _l_(20885)

    body[ind] += empty * (lens_max - length)
    _l_(20884)
