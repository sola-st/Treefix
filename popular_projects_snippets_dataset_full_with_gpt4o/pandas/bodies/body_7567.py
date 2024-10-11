# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_conversion.py
result = idx.to_numpy()
exp = idx.values
tm.assert_numpy_array_equal(result, exp)
