# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/12392
# equivalence of the labels/axis and index/columns API's
df = DataFrame(
    [[1, 2, 3], [3, 4, 5], [5, 6, 7]],
    index=["a", "b", "c"],
    columns=["d", "e", "f"],
)

res1 = df.reindex(["b", "a"])
res2 = df.reindex(index=["b", "a"])
res3 = df.reindex(labels=["b", "a"])
res4 = df.reindex(labels=["b", "a"], axis=0)
res5 = df.reindex(["b", "a"], axis=0)
for res in [res2, res3, res4, res5]:
    tm.assert_frame_equal(res1, res)

res1 = df.reindex(columns=["e", "d"])
res2 = df.reindex(["e", "d"], axis=1)
res3 = df.reindex(labels=["e", "d"], axis=1)
for res in [res2, res3]:
    tm.assert_frame_equal(res1, res)

res1 = df.reindex(index=["b", "a"], columns=["e", "d"])
res2 = df.reindex(columns=["e", "d"], index=["b", "a"])
res3 = df.reindex(labels=["b", "a"], axis=0).reindex(labels=["e", "d"], axis=1)
for res in [res2, res3]:
    tm.assert_frame_equal(res1, res)
