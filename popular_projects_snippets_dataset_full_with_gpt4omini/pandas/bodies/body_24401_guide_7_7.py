import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

body = ['apple', 'banana', 'kiwi', 'peach'] # pragma: no cover
data = [len(elem) for elem in body] # pragma: no cover
lens = Series(data) # pragma: no cover
lens_max = lens.max() # pragma: no cover
not_max = lens[lens != lens_max] # pragma: no cover
empty = [''] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/html.py
from l3.Runtime import _l_
data = [len(elem) for elem in body]
_l_(10126)
lens = Series(data)
_l_(10127)
lens_max = lens.max()
_l_(10128)
not_max = lens[lens != lens_max]
_l_(10129)

empty = [""]
_l_(10130)
for ind, length in not_max.items():
    _l_(10132)

    body[ind] += empty * (lens_max - length)
    _l_(10131)
