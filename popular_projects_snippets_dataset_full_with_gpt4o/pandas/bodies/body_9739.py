# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
x = x.between_time("09:00", "16:00")
exit(getattr(x.rolling(5, min_periods=1), f)())
