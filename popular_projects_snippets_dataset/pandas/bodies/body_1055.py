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
