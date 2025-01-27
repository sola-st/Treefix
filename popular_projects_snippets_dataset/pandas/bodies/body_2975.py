# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#9727
df = DataFrame([[1.0, 2.0], [3.0, 4.0]])
tm.assert_frame_equal(
    df.diff(axis=1), DataFrame([[np.nan, 1.0], [np.nan, 1.0]])
)
tm.assert_frame_equal(
    df.diff(axis=0), DataFrame([[np.nan, np.nan], [2.0, 2.0]])
)
