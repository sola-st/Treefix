# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_compare.py
# GH#30429
s1 = pd.Series(["a", "b", "c"])
s2 = pd.Series(["x", "b", "z"])

result = s1.compare(s2, align_axis=align_axis)

if align_axis in (1, "columns"):
    indices = pd.Index([0, 2])
    columns = pd.Index(["self", "other"])
    expected = pd.DataFrame(
        [["a", "x"], ["c", "z"]], index=indices, columns=columns
    )
    tm.assert_frame_equal(result, expected)
else:
    indices = pd.MultiIndex.from_product([[0, 2], ["self", "other"]])
    expected = pd.Series(["a", "x", "c", "z"], index=indices)
    tm.assert_series_equal(result, expected)
