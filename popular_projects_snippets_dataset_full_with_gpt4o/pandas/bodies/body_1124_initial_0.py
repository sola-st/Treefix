import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pytest # pragma: no cover

frame_random_data_integer_multi_index = pd.DataFrame(np.random.randint(0, 10, size=(4, 4)), index=pd.MultiIndex.from_product([[0, 1], [2, 3]])) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
from l3.Runtime import _l_
df = frame_random_data_integer_multi_index
_l_(21169)
with pytest.raises(KeyError, match=r"^3$"):
    _l_(21171)

    df.loc[3]
    _l_(21170)
