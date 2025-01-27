# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# gh-5986: Test timedelta types.

s = Series(
    ["1 days", "-1 days", "0 days", "nan", "nan"], dtype="timedelta64[ns]"
)
result = s.mode(dropna)
expected1 = Series(expected1, dtype="timedelta64[ns]")
tm.assert_series_equal(result, expected1)

s = Series(
    [
        "1 day",
        "1 day",
        "-1 day",
        "-1 day 2 min",
        "2 min",
        "2 min",
        "nan",
        "nan",
    ],
    dtype="timedelta64[ns]",
)
result = s.mode(dropna)
expected2 = Series(expected2, dtype="timedelta64[ns]")
tm.assert_series_equal(result, expected2)
