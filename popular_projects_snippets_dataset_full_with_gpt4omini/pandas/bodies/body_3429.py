# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
# issue 8839
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
ts = DataFrame(np.random.randn(len(rng), len(rng)))
ts.index, ts.columns = rng, rng

indices = rng[(rng.hour == 9) & (rng.minute == 30) & (rng.second == 0)]

if axis in ["index", 0]:
    expected = ts.loc[indices, :]
elif axis in ["columns", 1]:
    expected = ts.loc[:, indices]

result = ts.at_time("9:30", axis=axis)

# Without clearing freq, result has freq 1440T and expected 5T
result.index = result.index._with_freq(None)
expected.index = expected.index._with_freq(None)
tm.assert_frame_equal(result, expected)
