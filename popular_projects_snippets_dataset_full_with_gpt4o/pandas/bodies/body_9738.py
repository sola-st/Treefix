# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

# simple comparison of integer vs time-based windowing
df = regular * 2
er = df.rolling(window=1)
r = df.rolling(window="1s")

result = getattr(r, f)()
expected = getattr(er, f)()
tm.assert_frame_equal(result, expected)

result = r.quantile(0.5)
expected = er.quantile(0.5)
tm.assert_frame_equal(result, expected)
