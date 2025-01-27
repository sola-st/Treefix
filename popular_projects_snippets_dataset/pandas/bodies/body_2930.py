# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_period.py
dr = date_range("1/1/2000", "1/1/2001")
df = DataFrame(np.random.randn(len(dr), 5), index=dr)
df["mix"] = "a"

df = df.T
pts = df.to_period(axis=1)
exp = df.copy()
exp.columns = period_range("1/1/2000", "1/1/2001")
tm.assert_frame_equal(pts, exp)

pts = df.to_period("M", axis=1)
tm.assert_index_equal(pts.columns, exp.columns.asfreq("M"))
