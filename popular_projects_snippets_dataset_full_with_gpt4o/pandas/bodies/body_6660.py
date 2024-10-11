# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py
result = RangeIndex(range(1, 5, 2))
expected = RangeIndex(1, 5, 2)
tm.assert_index_equal(result, expected, exact=True)
