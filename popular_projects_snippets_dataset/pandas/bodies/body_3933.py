# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
ymd = multiindex_year_month_day_dataframe_random_data

# regular roundtrip
unstacked = ymd.unstack()
restacked = unstacked.stack()
tm.assert_frame_equal(restacked, ymd)

unlexsorted = ymd.sort_index(level=2)

unstacked = unlexsorted.unstack(2)
restacked = unstacked.stack()
tm.assert_frame_equal(restacked.sort_index(level=0), ymd)

unlexsorted = unlexsorted[::-1]
unstacked = unlexsorted.unstack(1)
restacked = unstacked.stack().swaplevel(1, 2)
tm.assert_frame_equal(restacked.sort_index(level=0), ymd)

unlexsorted = unlexsorted.swaplevel(0, 1)
unstacked = unlexsorted.unstack(0).swaplevel(0, 1, axis=1)
restacked = unstacked.stack(0).swaplevel(1, 2)
tm.assert_frame_equal(restacked.sort_index(level=0), ymd)

# columns unsorted
unstacked = ymd.unstack()
unstacked = unstacked.sort_index(axis=1, ascending=False)
restacked = unstacked.stack()
tm.assert_frame_equal(restacked, ymd)

# more than 2 levels in the columns
unstacked = ymd.unstack(1).unstack(1)

result = unstacked.stack(1)
expected = ymd.unstack()
tm.assert_frame_equal(result, expected)

result = unstacked.stack(2)
expected = ymd.unstack(1)
tm.assert_frame_equal(result, expected)

result = unstacked.stack(0)
expected = ymd.stack().unstack(1).unstack(1)
tm.assert_frame_equal(result, expected)

# not all levels present in each echelon
unstacked = ymd.unstack(2).loc[:, ::3]
stacked = unstacked.stack().stack()
ymd_stacked = ymd.stack()
tm.assert_series_equal(stacked, ymd_stacked.reindex(stacked.index))

# stack with negative number
result = ymd.unstack(0).stack(-2)
expected = ymd.unstack(0).stack(0)
tm.assert_equal(result, expected)
