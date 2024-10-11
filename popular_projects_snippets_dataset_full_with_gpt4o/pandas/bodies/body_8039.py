# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# see gh-15187
data = [np.nan]
expected = NumericIndex(data, dtype=np.float64)
result = Index(data, dtype="float")
tm.assert_index_equal(result, expected)
