# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 15494
# setting on frame with single row
df = DataFrame({"date": Series([Timestamp("20180101")])})
df.loc[:, "date"] = "string"
expected = DataFrame({"date": Series(["string"])})
tm.assert_frame_equal(df, expected)
