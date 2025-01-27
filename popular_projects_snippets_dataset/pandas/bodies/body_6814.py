# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH#37968
dti = date_range("2016-01-01", periods=9, tz=tz)
idx = IntervalIndex.from_breaks(dti)
mask = np.zeros(idx.shape, dtype=bool)
mask[0:3] = True

result = idx.putmask(mask, idx[-1])
expected = IntervalIndex([idx[-1]] * 3 + list(idx[3:]))
tm.assert_index_equal(result, expected)
