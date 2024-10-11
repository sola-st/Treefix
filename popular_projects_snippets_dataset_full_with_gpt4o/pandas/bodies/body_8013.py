# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
dti = date_range("2016-01-01", periods=3)
ii = IntervalIndex.from_breaks(dti)
result = Index(ii, dtype="category")
expected = CategoricalIndex(ii)
tm.assert_index_equal(result, expected)
