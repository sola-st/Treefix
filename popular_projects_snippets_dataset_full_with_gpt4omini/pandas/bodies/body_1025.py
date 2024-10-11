# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_partial.py
# GH #397
ymd = multiindex_year_month_day_dataframe_random_data
df = ymd.copy()
exp = ymd.copy()
df.loc[2000, 4] = 0
exp.iloc[65:85] = 0
tm.assert_frame_equal(df, exp)

df["A"].loc[2000, 4] = 1
if not using_copy_on_write:
    exp["A"].loc[2000, 4].values[:] = 1
tm.assert_frame_equal(df, exp)

df.loc[2000] = 5
exp.iloc[:100] = 5
tm.assert_frame_equal(df, exp)

# this works...for now
df["A"].iloc[14] = 5
if using_copy_on_write:
    df["A"].iloc[14] == exp["A"].iloc[14]
else:
    assert df["A"].iloc[14] == 5
