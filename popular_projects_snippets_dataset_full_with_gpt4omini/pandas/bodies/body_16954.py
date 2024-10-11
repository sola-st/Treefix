# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH#12467
# combining datetime tz-aware and naive DataFrames
ts1 = Timestamp("2015-01-01", tz=None)
ts2 = Timestamp("2015-01-01", tz="UTC")
ts3 = Timestamp("2015-01-01", tz="EST")

df1 = DataFrame({"time": [ts1]})
df2 = DataFrame({"time": [ts2]})
df3 = DataFrame({"time": [ts3]})

results = concat([df1, df2]).reset_index(drop=True)
expected = DataFrame({"time": [ts1, ts2]}, dtype=object)
tm.assert_frame_equal(results, expected)

results = concat([df1, df3]).reset_index(drop=True)
expected = DataFrame({"time": [ts1, ts3]}, dtype=object)
tm.assert_frame_equal(results, expected)

results = concat([df2, df3]).reset_index(drop=True)
expected = DataFrame({"time": [ts2, ts3]})
tm.assert_frame_equal(results, expected)
