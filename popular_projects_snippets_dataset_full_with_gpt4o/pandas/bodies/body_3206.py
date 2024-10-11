# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
rng = date_range("1/1/2000 09:30", periods=20)
norm = date_range("1/1/2000", periods=20)

vals = np.random.randn(20, 3)

obj = DataFrame(vals, index=rng)
expected = DataFrame(vals, index=norm)
if frame_or_series is Series:
    obj = obj[0]
    expected = expected[0]

result = obj.asfreq("D", normalize=True)
tm.assert_equal(result, expected)
