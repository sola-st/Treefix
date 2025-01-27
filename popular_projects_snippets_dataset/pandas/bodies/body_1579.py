# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#9516
dt1 = Timestamp("20130101 09:00:00")
dt2 = Timestamp("20130101 10:00:00")
df = DataFrame()
df.loc[conv(dt1), "one"] = 100
df.loc[conv(dt2), "one"] = 200

expected = DataFrame({"one": [100.0, 200.0]}, index=[dt1, dt2])
tm.assert_frame_equal(df, expected)
