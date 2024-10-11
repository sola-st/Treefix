# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH#22796
# Concatenating tz-aware multicolumn DataFrames
ts1 = Timestamp(t1, tz="UTC")
ts2 = Timestamp("2015-01-01", tz="UTC")
ts3 = Timestamp("2015-01-01", tz="UTC")

df1 = DataFrame([[ts1, ts2]])
df2 = DataFrame([[ts3]])

result = concat([df1, df2])
expected = DataFrame([[ts1, ts2], [ts3, pd.NaT]], index=[0, 0])

tm.assert_frame_equal(result, expected)
