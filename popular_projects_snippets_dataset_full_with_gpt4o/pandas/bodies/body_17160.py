# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH #1181

data = DataFrame(
    {
        "a": ["a", "a", "a", "a", "b", "b", "b", "b"] * 2,
        "b": [0, 0, 0, 0, 1, 1, 1, 1] * 2,
        "c": (["foo"] * 4 + ["bar"] * 4) * 2,
        "value": np.random.randn(16),
    }
)

table = data.pivot_table("value", index="a", columns=["b", "c"])

grouped = data.groupby(["a", "b", "c"])["value"].mean()
expected = grouped.unstack("b").unstack("c").dropna(axis=1, how="all")
tm.assert_frame_equal(table, expected)
