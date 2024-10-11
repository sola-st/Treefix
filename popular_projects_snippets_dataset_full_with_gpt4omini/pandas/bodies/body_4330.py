# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# https://github.com/pandas-dev/pandas/issues/35194
df1 = DataFrame(data=[[0]], columns=["second"])
df2 = DataFrame(data=[[0, 0, 0]], columns=["first", "second", "second"])
result = df1 + df2
expected = DataFrame([[np.nan, 0, 0]], columns=["first", "second", "second"])
tm.assert_frame_equal(result, expected)
