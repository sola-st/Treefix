# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# Test grouped Series
ser = pd.Series([1, 2, 3, 4, 5], index=["a", "a", "a", "b", "b"])
grouped = ser.groupby(level=0)
result = grouped._positional_selector[1:2]
expected = pd.Series([2, 5], index=["a", "b"])

tm.assert_series_equal(result, expected)
