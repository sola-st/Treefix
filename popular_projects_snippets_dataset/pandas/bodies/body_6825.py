# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 21243/21253

breaks = np.arange(10, dtype="int64")
expected = IntervalIndex.from_breaks(breaks)

cat_breaks = cat_constructor(breaks)
result_kwargs = self.get_kwargs_from_breaks(cat_breaks)
result = constructor(**result_kwargs)
tm.assert_index_equal(result, expected)
