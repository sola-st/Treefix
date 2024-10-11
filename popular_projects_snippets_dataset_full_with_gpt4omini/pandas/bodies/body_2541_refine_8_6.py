import pandas as pd # pragma: no cover
import pytest # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
def mock_raises(*args, **kwargs):# pragma: no cover
    class ContextManager:# pragma: no cover
        def __enter__(self):# pragma: no cover
            return self# pragma: no cover
        def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
            return False# pragma: no cover
    return ContextManager()# pragma: no cover
pytest = type('MockPytest', (object,), {'raises': staticmethod(mock_raises)})() # pragma: no cover

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
