import pandas as pd # pragma: no cover
import pytest # pragma: no cover

frame_random_data_integer_multi_index = pd.DataFrame({1: [1, 2], 2: [3, 4], 3: [5, 6]}) # pragma: no cover
frame_random_data_integer_multi_index.index = pd.MultiIndex.from_tuples([(0, 0), (1, 0)]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
from l3.Runtime import _l_
df = frame_random_data_integer_multi_index
_l_(10324)
with pytest.raises(KeyError, match=r"^3$"):
    _l_(10326)

    df.loc[3]
    _l_(10325)
