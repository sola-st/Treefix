# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#35465
result = Series([1000000, 200000, 3000000], dtype="timedelta64[ns]").astype(
    "int64"
)
expected = Series([1000000, 200000, 3000000], dtype="timedelta64[s]").astype(
    "int64"
)
tm.assert_series_equal(result, expected)
