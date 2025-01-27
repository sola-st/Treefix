# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
ymd = multiindex_year_month_day_dataframe_random_data

unstacked = ymd.unstack(["year", "month"])
expected = ymd.unstack("year").unstack("month")
tm.assert_frame_equal(unstacked, expected)
assert unstacked.columns.names == expected.columns.names

# series
s = ymd["A"]
s_unstacked = s.unstack(["year", "month"])
tm.assert_frame_equal(s_unstacked, expected["A"])

restacked = unstacked.stack(["year", "month"])
restacked = restacked.swaplevel(0, 1).swaplevel(1, 2)
restacked = restacked.sort_index(level=0)

tm.assert_frame_equal(restacked, ymd)
assert restacked.index.names == ymd.index.names

# GH #451
unstacked = ymd.unstack([1, 2])
expected = ymd.unstack(1).unstack(1).dropna(axis=1, how="all")
tm.assert_frame_equal(unstacked, expected)

unstacked = ymd.unstack([2, 1])
expected = ymd.unstack(2).unstack(1).dropna(axis=1, how="all")
tm.assert_frame_equal(unstacked, expected.loc[:, unstacked.columns])
