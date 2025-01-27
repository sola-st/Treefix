# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_dropna.py
ser = pd.Series([1, 2, 3, 3], index=idx)

result = ser.groupby(level=0, dropna=dropna).sum()
tm.assert_series_equal(result, expected)
