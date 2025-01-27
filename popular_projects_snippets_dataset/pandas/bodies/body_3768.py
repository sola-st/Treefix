# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_assign.py
df = DataFrame([[1, 4], [2, 5], [3, 6]], columns=["A", "B"])
result = df.assign(C=[7, 8, 9], D=df.A, E=lambda x: x.B)
expected = DataFrame(
    [[1, 4, 7, 1, 4], [2, 5, 8, 2, 5], [3, 6, 9, 3, 6]], columns=list("ABCDE")
)
tm.assert_frame_equal(result, expected)
