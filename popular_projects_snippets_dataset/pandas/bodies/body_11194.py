# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
dups = rand_series_with_duplicate_datetimeindex
result = dups.groupby(level=0).mean()
expected = dups.groupby(dups.index).mean()
tm.assert_series_equal(result, expected)
