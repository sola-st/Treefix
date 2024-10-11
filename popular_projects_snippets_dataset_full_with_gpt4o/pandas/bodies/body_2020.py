# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH#50505
ser = Series([val], dtype=object)
result = to_numeric(ser, use_nullable_dtypes=True)
expected = Series([val], dtype=dtype)
tm.assert_series_equal(result, expected)
