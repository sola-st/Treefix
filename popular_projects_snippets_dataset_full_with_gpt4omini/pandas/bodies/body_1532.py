# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#10583
df = DataFrame(np.random.normal(size=(10, 4)))
df.index = timedelta_range(start="0s", periods=10, freq="s")
expected = df.loc[Timedelta("0s") :, :]
result = df.loc["0s":, :]
tm.assert_frame_equal(result, expected)
