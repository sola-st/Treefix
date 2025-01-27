# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
result = index.isin(values)
tm.assert_numpy_array_equal(result, expected)
