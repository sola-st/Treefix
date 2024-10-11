# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
tdc = converter.TimeSeries_TimedeltaFormatter
result = tdc.format_timedelta_ticks(x, pos=None, n_decimals=decimal)
assert result == format_expected
