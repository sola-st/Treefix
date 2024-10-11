import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import numpy.testing as tm # pragma: no cover

multiindex_dataframe_random_data = pd.DataFrame(np.random.rand(4, 4), columns=pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'two')])) # pragma: no cover
tm = type('Mock', (object,), {'assert_almost_equal': staticmethod(tm.assert_almost_equal)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
from l3.Runtime import _l_
df = multiindex_dataframe_random_data.T
_l_(10820)
expected = df.values[:, 0]
_l_(10821)
result = df["foo", "one"].values
_l_(10822)
tm.assert_almost_equal(result, expected)
_l_(10823)
