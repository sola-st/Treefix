import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from pandas import Index, MultiIndex # pragma: no cover

Index = pd.Index # pragma: no cover
np = np # pragma: no cover
MultiIndex = pd.MultiIndex # pragma: no cover
tm = type('Mock', (), {'assert_index_equal': lambda x, y: None})() # pragma: no cover
pytest = type('Mock', (), {'raises': lambda exc_type, match: (lambda func: func)})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from pandas import Index, MultiIndex # pragma: no cover

Index = pd.Index # pragma: no cover
np = np # pragma: no cover
MultiIndex = pd.MultiIndex # pragma: no cover
tm = type('Mock', (), {'assert_index_equal': staticmethod(lambda x, y: x.equals(y))})() # pragma: no cover
class MockPytest:# pragma: no cover
    @staticmethod# pragma: no cover
    def raises(exc_type, match):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                return self# pragma: no cover
            def __exit__(self, exc_type_, exc_val, exc_tb):# pragma: no cover
                return exc_type_ == exc_type# pragma: no cover
        return ContextManager()# pragma: no cover
# pragma: no cover
pytest = MockPytest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
from l3.Runtime import _l_
idx = Index(["some_unequal_splits", "one_of_these_things_is_not", np.nan, None])
_l_(10631)
result = idx.str.split("_", expand=True)
_l_(10632)
exp = MultiIndex.from_tuples(
    [
        ("some", "unequal", "splits", np.nan, np.nan, np.nan),
        ("one", "of", "these", "things", "is", "not"),
        (np.nan, np.nan, np.nan, np.nan, np.nan, np.nan),
        (None, None, None, None, None, None),
    ]
)
_l_(10633)
tm.assert_index_equal(result, exp)
_l_(10634)
assert result.nlevels == 6
_l_(10635)

with pytest.raises(ValueError, match="expand must be"):
    _l_(10637)

    idx.str.split("_", expand="not_a_boolean")
    _l_(10636)
