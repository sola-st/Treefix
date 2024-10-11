# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
# These are by-definition the same with
# or without the index as the data is empty.
a = hash_pandas_object(obj, index=index)
b = hash_pandas_object(obj, index=index)
tm.assert_series_equal(a, b)
