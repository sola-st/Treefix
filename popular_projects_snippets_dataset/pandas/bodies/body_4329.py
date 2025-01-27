# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH #22663
expected = DataFrame([[0.0, np.nan], [3.0, np.nan]], columns=list("ab"))
expected = expected.astype({"b": col_dtype})
result = df + Series([-1.0], index=list("a"))
tm.assert_frame_equal(result, expected)
