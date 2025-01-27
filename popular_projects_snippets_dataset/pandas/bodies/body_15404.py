# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#32346
ser = Series([1, 2], dtype=dtype)
ser[indexer] = na
expected_values = [1, target_na] if indexer == 1 else [1, 2, target_na]
expected = Series(expected_values, dtype=target_dtype)
tm.assert_series_equal(ser, expected)
