# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# GH#19056
mi = MultiIndex.from_tuples(
    [("a", "x"), ("a", "y"), ("b", "x")], names=["level1", "level2"]
)
df = DataFrame([[1, 2, 3]], columns=mi)
result = df.xs("a", axis=1, drop_level=False)
expected = DataFrame(
    [[1, 2]],
    columns=MultiIndex.from_tuples(
        [("a", "x"), ("a", "y")], names=["level1", "level2"]
    ),
)
tm.assert_frame_equal(result, expected)
