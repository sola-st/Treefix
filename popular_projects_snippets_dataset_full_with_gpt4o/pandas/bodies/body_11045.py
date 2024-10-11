# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 38227
# GH#43205
df = DataFrame(
    {
        "col": [1, 2, 3, 4, 5],
        "group": ["a", np.nan, np.nan, "b", "b"],
    },
    index=list("xxyxz"),
)
result = df.groupby("group", dropna=dropna, group_keys=False).apply(lambda x: x)
expected = df.dropna() if dropna else df.iloc[[0, 3, 1, 2, 4]]
tm.assert_frame_equal(result, expected)
