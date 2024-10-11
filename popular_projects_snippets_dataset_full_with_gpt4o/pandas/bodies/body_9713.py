# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

# non-fixed freqs
msg = "\\<2 \\* MonthBegins\\> is a non-fixed frequency"
with pytest.raises(ValueError, match=msg):
    regular.rolling(window=freq)
