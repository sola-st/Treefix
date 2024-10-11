# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# drop buggy GH#6240
df = DataFrame(
    {
        "A": np.random.randn(5),
        "B": np.random.randn(5),
        "C": np.random.randn(5),
        "D": ["a", "b", "c", "d", "e"],
    }
)

expected = df.take([0, 1, 1], axis=1)
df2 = df.take([2, 0, 1, 2, 1], axis=1)
result = df2.drop("C", axis=1)
tm.assert_frame_equal(result, expected)
