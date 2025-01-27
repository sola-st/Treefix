# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_swapaxes.py
df = DataFrame(np.random.randn(10, 5))
tm.assert_frame_equal(df.T, df.swapaxes(0, 1))
tm.assert_frame_equal(df.T, df.swapaxes(1, 0))
