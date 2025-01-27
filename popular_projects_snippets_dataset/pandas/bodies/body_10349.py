# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH43926
df = DataFrame(
    [
        [4, 5, 6],
        [8, 8, 7],
    ],
    index=["z", "y"],
    columns=["C", "B", "A"],
)
result = df.groupby(df.iloc[1], axis=1).nth(0)
expected = df.iloc[:, [0, 2]]
tm.assert_frame_equal(result, expected)
