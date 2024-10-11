# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 16894
result = DataFrame({np.nan: [1, 2], 2: [2, 3]}, columns=[np.nan, 2])
expected = DataFrame([[1, 2], [2, 3]], columns=[np.nan, 2])
tm.assert_frame_equal(result, expected)
