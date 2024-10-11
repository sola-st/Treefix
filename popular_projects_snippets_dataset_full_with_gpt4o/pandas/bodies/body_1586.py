# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#11485
df = DataFrame({"A": [1, 2, 3, 4], "B": list("aabb"), "C": [1, 2, 3, 4]})
# iloc cannot use boolean Series (see GH3635)

# return bool indexer
res = df.loc[lambda x: x.A > 2]
tm.assert_frame_equal(res, df.loc[df.A > 2])

res = df.loc[lambda x: x.B == "b", :]
tm.assert_frame_equal(res, df.loc[df.B == "b", :])

res = df.loc[lambda x: x.A > 2, lambda x: x.columns == "B"]
tm.assert_frame_equal(res, df.loc[df.A > 2, [False, True, False]])

res = df.loc[lambda x: x.A > 2, lambda x: "B"]
tm.assert_series_equal(res, df.loc[df.A > 2, "B"])

res = df.loc[lambda x: x.A > 2, lambda x: ["A", "B"]]
tm.assert_frame_equal(res, df.loc[df.A > 2, ["A", "B"]])

res = df.loc[lambda x: x.A == 2, lambda x: ["A", "B"]]
tm.assert_frame_equal(res, df.loc[df.A == 2, ["A", "B"]])

# scalar
res = df.loc[lambda x: 1, lambda x: "A"]
assert res == df.loc[1, "A"]
