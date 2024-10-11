# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#32995 operate column-wise when we have mixed dtypes and axis=1
df = DataFrame({"A": range(3), "B": 2 * np.arange(3, dtype=np.float64)})

expected = df * np.nan

result = df.diff(axis=1, periods=3)
tm.assert_frame_equal(result, expected)
