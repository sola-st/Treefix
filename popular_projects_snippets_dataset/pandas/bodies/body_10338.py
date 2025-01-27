# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 20760
# Check that nth preserves column order
df = DataFrame(
    [[1, "b", 100], [1, "a", 50], [1, "a", np.nan], [2, "c", 200], [2, "d", 150]],
    columns=["A", "C", "B"],
)
result = df.groupby("A").nth(0)
expected = df.iloc[[0, 3]]
tm.assert_frame_equal(result, expected)

result = df.groupby("A").nth(-1, dropna="any")
expected = df.iloc[[1, 4]]
tm.assert_frame_equal(result, expected)
