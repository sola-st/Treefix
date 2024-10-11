# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
arr = series.values
tm.assert_numpy_array_equal(hash_array(arr), hash_array(arr))
