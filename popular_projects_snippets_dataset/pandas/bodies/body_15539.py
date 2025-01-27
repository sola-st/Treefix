# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_truncate.py
# GH 42365
obj = Series(0, index=date_range("2021-06-30", "2021-06-30")).repeat(5)

truncated = obj.truncate("2021-06-28", "2021-07-01")

tm.assert_series_equal(truncated, obj)
