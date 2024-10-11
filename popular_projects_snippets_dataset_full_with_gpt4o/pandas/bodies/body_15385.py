# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
ts = datetime_series
mask_shifted = ts.shift(1, freq=BDay()) > ts.median()

msg = (
    r"Unalignable boolean Series provided as indexer \(index of "
    r"the boolean Series and of the indexed object do not match"
)
with pytest.raises(IndexingError, match=msg):
    ts[mask_shifted] = 1

with pytest.raises(IndexingError, match=msg):
    ts.loc[mask_shifted] = 1
