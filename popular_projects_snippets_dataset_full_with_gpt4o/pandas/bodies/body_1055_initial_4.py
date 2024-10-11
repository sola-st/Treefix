import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

index = pd.MultiIndex.from_product([['foo', 'bar'], ['one', 'two']], names=['first', 'second']) # pragma: no cover
data = np.random.rand(4, 4) # pragma: no cover
multiindex_dataframe_random_data = pd.DataFrame(data, index=index, columns=index) # pragma: no cover
tm = type('Mock', (object,), {'assert_almost_equal': lambda x, y: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
from l3.Runtime import _l_
df = multiindex_dataframe_random_data.T
_l_(22411)
expected = df.values[:, 0]
_l_(22412)
result = df["foo", "one"].values
_l_(22413)
tm.assert_almost_equal(result, expected)
_l_(22414)
