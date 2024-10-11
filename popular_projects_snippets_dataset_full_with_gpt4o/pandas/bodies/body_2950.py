# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# GH 29132: test axis names
data = {0: [0, np.nan, 6], 1: [1, np.nan, 7], 2: [2, 5, 8]}

df = DataFrame(data, dtype=np.float64)
result = df.interpolate(axis=axis_name, method="linear")
expected = df.interpolate(axis=axis_number, method="linear")
tm.assert_frame_equal(result, expected)
