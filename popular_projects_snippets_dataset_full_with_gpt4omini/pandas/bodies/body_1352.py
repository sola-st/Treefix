# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH 20627
result = DataFrame([[0, 1], [2, 3], [4, 5], [6, np.nan]])
result.iloc[result.index <= 2] *= 2
expected = DataFrame([[0, 2], [4, 6], [8, 10], [6, np.nan]])
tm.assert_frame_equal(result, expected)

result.iloc[result.index > 2] *= 2
expected = DataFrame([[0, 2], [4, 6], [8, 10], [12, np.nan]])
tm.assert_frame_equal(result, expected)

result.iloc[[True, True, False, False]] *= 2
expected = DataFrame([[0, 4], [8, 12], [8, 10], [12, np.nan]])
tm.assert_frame_equal(result, expected)

result.iloc[[False, False, True, True]] /= 2
expected = DataFrame([[0, 4.0], [8, 12.0], [4, 5.0], [6, np.nan]])
tm.assert_frame_equal(result, expected)
