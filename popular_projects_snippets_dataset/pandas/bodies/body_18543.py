# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
tz = tz_aware_fixture
tz_didx = date_range("2000-01-01", "2020-01-01", freq=freq, tz=tz)
naive_didx = date_range("2000-01-01", "2020-01-01", freq=freq)

_compare_utc_to_local(tz_didx)
_compare_local_to_utc(tz_didx, naive_didx)
