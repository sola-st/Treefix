import pandas as pd # pragma: no cover
import pytest # pragma: no cover

frame_random_data_integer_multi_index = pd.DataFrame({0: [1, 2, 3]}, index=[0, 1, 2]).set_index(pd.MultiIndex.from_product([[0], [1, 2, 3]])) # pragma: no cover
pytest = type('MockPytest', (object,), {'raises': staticmethod(lambda exception_cls, match=None: (lambda func: func))}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
from l3.Runtime import _l_
df = frame_random_data_integer_multi_index
_l_(10324)
with pytest.raises(KeyError, match=r"^3$"):
    _l_(10326)

    df.loc[3]
    _l_(10325)
