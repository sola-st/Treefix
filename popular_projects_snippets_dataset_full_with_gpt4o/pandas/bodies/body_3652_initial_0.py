import pandas as pd # pragma: no cover

frame_or_series = pd.Series # pragma: no cover
MultiIndex = type('Mock', (object,), {'from_tuples': pd.MultiIndex.from_tuples}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
from l3.Runtime import _l_
obj = frame_or_series(
    [11, 21, 31],
    index=MultiIndex.from_tuples([("A", x) for x in ["a", "B", "c"]]),
)
_l_(21939)
obj.rename(str.lower)
_l_(21940)
