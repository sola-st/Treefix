# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# equivalence of the labels/axis and index/columns API's (GH#12392)
df = DataFrame(
    [[1, 2, 3], [3, 4, 5], [5, 6, 7]],
    index=["a", "b", "c"],
    columns=["d", "e", "f"],
)

res1 = df.drop("a")
res2 = df.drop(index="a")
tm.assert_frame_equal(res1, res2)

res1 = df.drop("d", axis=1)
res2 = df.drop(columns="d")
tm.assert_frame_equal(res1, res2)

res1 = df.drop(labels="e", axis=1)
res2 = df.drop(columns="e")
tm.assert_frame_equal(res1, res2)

res1 = df.drop(["a"], axis=0)
res2 = df.drop(index=["a"])
tm.assert_frame_equal(res1, res2)

res1 = df.drop(["a"], axis=0).drop(["d"], axis=1)
res2 = df.drop(index=["a"], columns=["d"])
tm.assert_frame_equal(res1, res2)

msg = "Cannot specify both 'labels' and 'index'/'columns'"
with pytest.raises(ValueError, match=msg):
    df.drop(labels="a", index="b")

with pytest.raises(ValueError, match=msg):
    df.drop(labels="a", columns="b")

msg = "Need to specify at least one of 'labels', 'index' or 'columns'"
with pytest.raises(ValueError, match=msg):
    df.drop(axis=1)
