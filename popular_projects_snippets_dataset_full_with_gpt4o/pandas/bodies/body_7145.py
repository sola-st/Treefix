# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH 8608
# add/sub are overridden explicitly for Float/Int Index
index_cls = self._index_cls
if index_cls is RangeIndex:
    idx = RangeIndex(5)
else:
    idx = index_cls(np.arange(5, dtype="int64"))

# float conversions
arr = np.arange(5, dtype="int64") * 3.2
expected = NumericIndex(arr, dtype=np.float64)
fidx = idx * 3.2
tm.assert_index_equal(fidx, expected)
fidx = 3.2 * idx
tm.assert_index_equal(fidx, expected)

# interops with numpy arrays
expected = NumericIndex(arr, dtype=np.float64)
a = np.zeros(5, dtype="float64")
result = fidx - a
tm.assert_index_equal(result, expected)

expected = NumericIndex(-arr, dtype=np.float64)
a = np.zeros(5, dtype="float64")
result = a - fidx
tm.assert_index_equal(result, expected)
