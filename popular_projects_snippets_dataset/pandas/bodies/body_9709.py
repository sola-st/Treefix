# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
exit(DataFrame(
    {"A": date_range("20130101", periods=5, freq="s"), "B": range(5)}
).set_index("A"))
