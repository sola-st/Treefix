# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
# GH27721
df = concat(
    {
        "a": DataFrame({"col1": [3, 4], "col2": [1, 2]}),
        "b": DataFrame({"col3": [5, 6], "col4": [7, 8]}),
    },
    axis=1,
)

gb = df.groupby(level=0, axis=1)
result = gb.rank(axis=1)

expected = concat(
    [
        df["a"].rank(axis=1),
        df["b"].rank(axis=1),
    ],
    axis=1,
    keys=["a", "b"],
)
tm.assert_frame_equal(result, expected)
