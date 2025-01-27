# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 9772
df = DataFrame(
    [[1, 2, 3], [1, 4, 5], [2, 6, 7], [3, 8, 9]], columns=["A", "B", "C"]
)
g = df.groupby([0, 0, 1], axis=1)
expected = df.iloc[:, expected_cols]
result = getattr(g, op)(n)
tm.assert_frame_equal(result, expected)
