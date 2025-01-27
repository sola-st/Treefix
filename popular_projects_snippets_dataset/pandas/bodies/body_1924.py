# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
idx = date_range(start="8/15/2012", periods=100, freq=from_freq)
df = DataFrame(np.random.randn(len(idx), 2), idx)

resampled = df.resample(to_freq).mean()
tm.assert_frame_equal(
    resampled, df.resample(to_freq, closed="left", label="left").mean()
)
