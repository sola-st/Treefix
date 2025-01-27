# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
per = pd.PeriodIndex([datetime(2003, 1, 1, 12), None], freq="H")

# Default formatting
formatted = per.format()
assert formatted[0] == "2003-01-01 12:00"  # default: minutes not shown
assert formatted[1] == "NaT"
# format is equivalent to strftime(None)...
assert formatted[0] == per.strftime(None)[0]
assert per.strftime(None)[1] is np.nan  # ...except for NaTs

# Same test with nanoseconds freq
per = pd.period_range("2003-01-01 12:01:01.123456789", periods=2, freq="n")
formatted = per.format()
assert (formatted == per.strftime(None)).all()
assert formatted[0] == "2003-01-01 12:01:01.123456789"
assert formatted[1] == "2003-01-01 12:01:01.123456790"
