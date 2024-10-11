# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
halflife = halflife_with_times
data = np.arange(10.0)
data[::2] = np.nan
df = DataFrame({"A": data})
result = df.ewm(halflife=halflife, min_periods=min_periods, times=times).mean()
expected = df.ewm(halflife=1.0, min_periods=min_periods).mean()
tm.assert_frame_equal(result, expected)
