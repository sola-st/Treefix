import pandas as pd # pragma: no cover
import pytest # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
pytest.raises = type('Mock', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_val, exc_tb: issubclass(exc_type, ValueError) and 'Columns must be same length as key' == str(exc_val)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#39510
from l3.Runtime import _l_
cols = ["A", "B", "C"] * 2
_l_(21540)
df = DataFrame(index=range(3), columns=cols)
_l_(21541)
with pytest.raises(ValueError, match="Columns must be same length as key"):
    _l_(21543)

    df[["A"]] = (0, 3, 5)
    _l_(21542)

df2 = df.iloc[:, :3]  # unique columns
_l_(21544)  # unique columns
with pytest.raises(ValueError, match="Columns must be same length as key"):
    _l_(21546)

    df2[["A"]] = (0, 3, 5)
    _l_(21545)
