# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#35465
result = Series([1000000, 200000, 3000000], dtype="timedelta64[ns]")
expected = Series(pd.to_timedelta([1000000, 200000, 3000000], unit="ns"))
tm.assert_series_equal(result, expected)
