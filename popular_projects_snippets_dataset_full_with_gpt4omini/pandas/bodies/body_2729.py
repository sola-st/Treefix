# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_clip.py
"""Should process np.nan argument as None"""
# GH#17276
tm.assert_frame_equal(float_frame.clip(np.nan), float_frame)
tm.assert_frame_equal(float_frame.clip(upper=np.nan, lower=np.nan), float_frame)

# GH#19992 and adjusted in GH#40420
df = DataFrame({"col_0": [1, 2, 3], "col_1": [4, 5, 6], "col_2": [7, 8, 9]})

result = df.clip(lower=[4, 5, np.nan], axis=0)
expected = DataFrame(
    {"col_0": [4, 5, 3], "col_1": [4, 5, 6], "col_2": [7, 8, 9]}
)
tm.assert_frame_equal(result, expected)

result = df.clip(lower=[4, 5, np.nan], axis=1)
expected = DataFrame(
    {"col_0": [4, 4, 4], "col_1": [5, 5, 6], "col_2": [7, 8, 9]}
)
tm.assert_frame_equal(result, expected)

# GH#40420
data = {"col_0": [9, -3, 0, -1, 5], "col_1": [-2, -7, 6, 8, -5]}
df = DataFrame(data)
t = Series([2, -4, np.NaN, 6, 3])
result = df.clip(lower=t, axis=0)
expected = DataFrame({"col_0": [9, -3, 0, 6, 5], "col_1": [2, -4, 6, 8, 3]})
tm.assert_frame_equal(result, expected)
