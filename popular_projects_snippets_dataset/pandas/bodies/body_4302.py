# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
rng = pd.period_range("1/1/2000", "1/1/2010", freq="A")
ts = DataFrame(np.random.randn(len(rng), 3), index=rng)

result = ts + ts[::2]
expected = ts + ts
expected.iloc[1::2] = np.nan
tm.assert_frame_equal(result, expected)

half = ts[::2]
result = ts + half.take(np.random.permutation(len(half)))
tm.assert_frame_equal(result, expected)
