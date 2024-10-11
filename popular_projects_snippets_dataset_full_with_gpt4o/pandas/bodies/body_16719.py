# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 16572
# Check that float column is not cast to object if
# merging on float and int columns
A = DataFrame({"X": int_vals})
B = DataFrame({"Y": float_vals})
expected = DataFrame(exp_vals)

result = A.merge(B, left_on="X", right_on="Y")
tm.assert_frame_equal(result, expected)

result = B.merge(A, left_on="Y", right_on="X")
tm.assert_frame_equal(result, expected[["Y", "X"]])
