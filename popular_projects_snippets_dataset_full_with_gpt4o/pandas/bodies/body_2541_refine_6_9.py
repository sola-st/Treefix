import pandas as pd # pragma: no cover
import pytest # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
pytest.raises = type('Mock', (object,), {'__call__': pytest.raises}) # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
class MockRaises:# pragma: no cover
    def __init__(self, expected_exception, match=None):# pragma: no cover
        self.expected_exception = expected_exception# pragma: no cover
        self.match = match# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
        if not exc_type:# pragma: no cover
            raise AssertionError('DID NOT RAISE')# pragma: no cover
        if not issubclass(exc_type, self.expected_exception):# pragma: no cover
            raise AssertionError(f'RAISED WRONG EXCEPTION: {exc_type}')# pragma: no cover
        if self.match and self.match not in str(exc_val):# pragma: no cover
            raise AssertionError(f'EXCEPTION MATCH FAILED: {exc_val}')# pragma: no cover
        return True# pragma: no cover
pytest.raises = lambda expected_exception, match=None: MockRaises(expected_exception, match) # pragma: no cover

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
