# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# Calling the following sum functions returned an error for dataframes but
# returned NaT for series. These tests check that the API is consistent in
# min/max calls on empty Series/DataFrames. See GH:33704 for more
# information
df = DataFrame({"x": to_datetime([])})
expected_dt_series = Series(to_datetime([]))
# check axis 0
assert (df.min(axis=0).x is pd.NaT) == (expected_dt_series.min() is pd.NaT)
assert (df.max(axis=0).x is pd.NaT) == (expected_dt_series.max() is pd.NaT)

# check axis 1
tm.assert_series_equal(df.min(axis=1), expected_dt_series)
tm.assert_series_equal(df.max(axis=1), expected_dt_series)
