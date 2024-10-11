# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

N = 10000

dfp = DataFrame(
    {"B": np.random.randn(N)}, index=date_range("20130101", periods=N, freq="s")
)
expected = dfp.rolling(2, min_periods=1).min()
result = dfp.rolling("2s").min()
assert ((result - expected) < 0.01).all().bool()

expected = dfp.rolling(200, min_periods=1).min()
result = dfp.rolling("200s").min()
assert ((result - expected) < 0.01).all().bool()
