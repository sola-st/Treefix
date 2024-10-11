# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
rng = date_range("1/1/2000", periods=20)
ts = frame_or_series(np.random.randn(20), index=rng)

ts2 = ts.copy()
ts2.index = [x.date() for x in ts2.index]

result = ts2.asfreq("4H", method="ffill")
expected = ts.asfreq("4H", method="ffill")
tm.assert_equal(result, expected)
