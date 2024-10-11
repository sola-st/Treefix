import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

index = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'two')], names=['first', 'second']) # pragma: no cover
multiindex_dataframe_random_data = pd.DataFrame(np.random.randn(4, 4), index=index, columns=index) # pragma: no cover
class Mock: pass # pragma: no cover
tm = Mock() # pragma: no cover

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
