# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 16572
# merge will produce a warning when merging on int and
# float columns where the float values are not exactly
# equal to their int representation
A = DataFrame({"X": [1, 2, 3]})
B = DataFrame({"Y": [1.1, 2.5, 3.0]})
expected = DataFrame({"X": [3], "Y": [3.0]})

with tm.assert_produces_warning(UserWarning):
    result = A.merge(B, left_on="X", right_on="Y")
    tm.assert_frame_equal(result, expected)

with tm.assert_produces_warning(UserWarning):
    result = B.merge(A, left_on="Y", right_on="X")
    tm.assert_frame_equal(result, expected[["Y", "X"]])

# test no warning if float has NaNs
B = DataFrame({"Y": [np.nan, np.nan, 3.0]})

with tm.assert_produces_warning(None):
    result = B.merge(A, left_on="Y", right_on="X")
    tm.assert_frame_equal(result, expected[["Y", "X"]])
