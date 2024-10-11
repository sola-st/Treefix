# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
# Matplotlib's time representation using floats cannot distinguish
# intervals smaller than ~10 microsecond in the common range of years.
ts1 = Timestamp("2012-1-1")
ts2 = ts1 + offset
val1 = dtc.convert(ts1, None, None)
val2 = dtc.convert(ts2, None, None)
if not val1 < val2:
    raise AssertionError(f"{val1} is not less than {val2}.")
