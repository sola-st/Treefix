# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
dti = date_range("2016-01-01", periods=3)
result = Index(dti, dtype="category")
expected = CategoricalIndex(dti)
tm.assert_index_equal(result, expected)

dti2 = date_range("2016-01-01", periods=3, tz="US/Pacific")
result = Index(dti2, dtype="category")
expected = CategoricalIndex(dti2)
tm.assert_index_equal(result, expected)
