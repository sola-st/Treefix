import pandas as pd # pragma: no cover
import pytest # pragma: no cover

DataFrame = type('Mock', (object,), {'__init__': lambda self, index, columns: None, '__setitem__': lambda self, key, value: None, 'iloc': lambda self, key: self}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#39510
from l3.Runtime import _l_
cols = ["A", "B", "C"] * 2
_l_(10382)
df = DataFrame(index=range(3), columns=cols)
_l_(10383)
with pytest.raises(ValueError, match="Columns must be same length as key"):
    _l_(10385)

    df[["A"]] = (0, 3, 5)
    _l_(10384)

df2 = df.iloc[:, :3]  # unique columns
_l_(10386)  # unique columns
with pytest.raises(ValueError, match="Columns must be same length as key"):
    _l_(10388)

    df2[["A"]] = (0, 3, 5)
    _l_(10387)
