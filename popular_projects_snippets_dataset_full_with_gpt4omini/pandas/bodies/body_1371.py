# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#2259
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=[1, 1, 2])
result = df.iloc[:, [0]]
expected = df.take([0], axis=1)
tm.assert_frame_equal(result, expected)
