# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2000", periods=2, freq="D", tz="US/Central")
arr = DatetimeArray(dti).repeat([4, 3])

result = arr.value_counts()

# Note: not tm.assert_index_equal, since `freq`s do not match
assert result.index.equals(dti)

arr[-2] = pd.NaT
result = arr.value_counts(dropna=False)
expected = pd.Series([4, 2, 1], index=[dti[0], dti[1], pd.NaT])
tm.assert_series_equal(result, expected)
