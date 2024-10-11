# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# broadcasting issue in GH 7325
df = DataFrame(np.arange(3 * 2).reshape((3, 2)), dtype=dtype)
expected = DataFrame([[np.nan, np.inf], [1.0, 1.5], [1.0, 1.25]])
result = df.div(df[0], axis="index")
tm.assert_frame_equal(result, expected)
