# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#910
X = np.arange(10 * 10, dtype="float64").reshape(10, 10)
Y = np.ones((10, 1), dtype=int)

df1 = DataFrame(X)
df1["0.X"] = Y.squeeze()

df2 = df1.astype(float)

result = df1 - df1.mean()
expected = df2 - df2.mean()
tm.assert_frame_equal(result, expected)
