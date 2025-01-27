# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_sorting.py
result = idx.argsort()
expected = idx.values.argsort()
tm.assert_numpy_array_equal(result, expected)
