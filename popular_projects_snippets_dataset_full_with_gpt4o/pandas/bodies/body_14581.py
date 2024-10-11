# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idx = date_range("12/31/1999", freq=freq, periods=100)
ser = Series(np.random.randn(len(idx)), idx)
ser = Series(ser.values, Index(np.asarray(ser.index)))
_check_plot_works(ser.plot, ser.index.inferred_freq)

ser = ser[[0, 3, 5, 6]]
_check_plot_works(ser.plot)
