# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
df = DataFrame(
    [[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=["bar", "a", "a"]
)
result = df.drop(["a"], axis=1)
expected = DataFrame([[1], [1], [1]], columns=["bar"])
tm.assert_frame_equal(result, expected)
result = df.drop("a", axis=1)
tm.assert_frame_equal(result, expected)
