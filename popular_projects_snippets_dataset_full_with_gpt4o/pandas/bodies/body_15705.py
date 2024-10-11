# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_compare.py
s1 = pd.Series(["a", "b", "c"])
s2 = pd.Series(["x", "b", "z"])

result = s1.compare(s2, keep_shape=keep_shape, keep_equal=keep_equal)

if keep_shape:
    indices = pd.Index([0, 1, 2])
    columns = pd.Index(["self", "other"])
    if keep_equal:
        expected = pd.DataFrame(
            [["a", "x"], ["b", "b"], ["c", "z"]], index=indices, columns=columns
        )
    else:
        expected = pd.DataFrame(
            [["a", "x"], [np.nan, np.nan], ["c", "z"]],
            index=indices,
            columns=columns,
        )
else:
    indices = pd.Index([0, 2])
    columns = pd.Index(["self", "other"])
    expected = pd.DataFrame(
        [["a", "x"], ["c", "z"]], index=indices, columns=columns
    )
tm.assert_frame_equal(result, expected)
