# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_indexing.py
# GH 31446
ser = pd.Series([1, 2], dtype="Int64")
result = ser.where(ser > 1)
expected = pd.Series([pd.NA, 2], dtype="Int64")
tm.assert_series_equal(result, expected)
