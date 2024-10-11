# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# see gh-23372.
df = DataFrame(np.ones((10, 20)))
axis = df._get_axis_number(axis_frame)

if axis == 0:
    expected = DataFrame({i: [np.nan] * 2 + [3.0] * 8 for i in range(20)})
else:
    # axis == 1
    expected = DataFrame([[np.nan] * 2 + [3.0] * 18] * 10)

result = df.rolling(3, axis=axis_frame).sum()
tm.assert_frame_equal(result, expected)
