# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_partial_slicing.py
# GH#5407
idx = make_range(start="2013/10/01", freq="D", periods=10)

df = DataFrame({"units": [100 + i for i in range(10)]}, index=idx)
empty = DataFrame(index=type(idx)([], freq="D"), columns=["units"])
empty["units"] = empty["units"].astype("int64")

tm.assert_frame_equal(df["2013/09/01":"2013/09/30"], empty)
tm.assert_frame_equal(df["2013/09/30":"2013/10/02"], df.iloc[:2])
tm.assert_frame_equal(df["2013/10/01":"2013/10/02"], df.iloc[:2])
tm.assert_frame_equal(df["2013/10/02":"2013/09/30"], empty)
tm.assert_frame_equal(df["2013/10/15":"2013/10/17"], empty)
tm.assert_frame_equal(df["2013-06":"2013-09"], empty)
tm.assert_frame_equal(df["2013-11":"2013-12"], empty)
