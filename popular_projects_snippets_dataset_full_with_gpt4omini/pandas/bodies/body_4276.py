# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#5185 dup aligning operations should work
df1 = DataFrame([1, 2, 3, 4, 5], index=[1, 2, 1, 2, 3])
df2 = DataFrame([1, 2, 3], index=[1, 2, 3])
expected = DataFrame([0, 2, 0, 2, 2], index=[1, 1, 2, 2, 3])
result = df1.sub(df2)
tm.assert_frame_equal(result, expected)
