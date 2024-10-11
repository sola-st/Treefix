# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# https://github.com/pandas-dev/pandas/issues/35559
arr = np.random.randn(5, 2)
arr.flags.writeable = False
df = DataFrame(arr)
result = df.diff()
expected = DataFrame(np.array(df)).diff()
tm.assert_frame_equal(result, expected)
