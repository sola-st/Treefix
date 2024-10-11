# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# check we don't silently ignore the dtype keyword
tdi = timedelta_range("4 Days", periods=5)
result = Index(tdi, dtype="category")
expected = CategoricalIndex(tdi)
tm.assert_index_equal(result, expected)
