# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 14467
result = DataFrame(
    [[1, 2, 3], [4, 5, 6]], columns=[["A", "A", "A"], ["a", "b", "c"]]
)
expected = DataFrame(
    [[1, 2, 3], [4, 5, 6]],
    columns=MultiIndex.from_tuples([("A", "a"), ("A", "b"), ("A", "c")]),
)
tm.assert_frame_equal(result, expected)
