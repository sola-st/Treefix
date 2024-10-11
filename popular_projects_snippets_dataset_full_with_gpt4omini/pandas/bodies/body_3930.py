# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# just check that it works for now
ymd = multiindex_year_month_day_dataframe_random_data

unstacked = ymd.unstack()
unstacked.unstack()

# test that ints work
ymd.astype(int).unstack()

# test that int32 work
ymd.astype(np.int32).unstack()
