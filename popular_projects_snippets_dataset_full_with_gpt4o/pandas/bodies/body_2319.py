# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 12533
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = df.where(lambda x: x > 4, lambda x: x + 1)
exp = DataFrame([[2, 3, 4], [5, 5, 6], [7, 8, 9]])
tm.assert_frame_equal(result, exp)
tm.assert_frame_equal(result, df.where(df > 4, df + 1))

# return ndarray and scalar
result = df.where(lambda x: (x % 2 == 0).values, lambda x: 99)
exp = DataFrame([[99, 2, 99], [4, 99, 6], [99, 8, 99]])
tm.assert_frame_equal(result, exp)
tm.assert_frame_equal(result, df.where(df % 2 == 0, 99))

# chain
result = (df + 2).where(lambda x: x > 8, lambda x: x + 10)
exp = DataFrame([[13, 14, 15], [16, 17, 18], [9, 10, 11]])
tm.assert_frame_equal(result, exp)
tm.assert_frame_equal(result, (df + 2).where((df + 2) > 8, (df + 2) + 10))
