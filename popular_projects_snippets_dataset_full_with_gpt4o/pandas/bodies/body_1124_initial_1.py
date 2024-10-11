import pandas as pd # pragma: no cover
import pytest # pragma: no cover

frame_random_data_integer_multi_index = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] }, index=pd.MultiIndex.from_tuples([(0, 1), (1, 2), (2, 3)])) # pragma: no cover
pytest = type('Mock', (object,), {'raises': pytest.raises}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
from l3.Runtime import _l_
df = frame_random_data_integer_multi_index
_l_(21169)
with pytest.raises(KeyError, match=r"^3$"):
    _l_(21171)

    df.loc[3]
    _l_(21170)
