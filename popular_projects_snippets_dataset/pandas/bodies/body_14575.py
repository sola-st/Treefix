# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idx = period_range("12/31/1999", freq=freq, periods=100)
ser = Series(np.random.randn(len(idx)), idx)
_check_plot_works(ser.plot, ser.index.freq)
