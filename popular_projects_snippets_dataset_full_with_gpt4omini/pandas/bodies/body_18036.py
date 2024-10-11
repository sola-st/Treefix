# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
a = hash_pandas_object(series, index=index)
b = hash_pandas_object(series, index=index)
tm.assert_series_equal(a, b)
