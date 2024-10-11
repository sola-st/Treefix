# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
daystr = f"2011-02-{num}"
freq = f"W-{day}"

result = Period(daystr, freq=freq)
expected = Period(daystr, freq="D").asfreq(freq)
assert result == expected
assert isinstance(result, Period)
