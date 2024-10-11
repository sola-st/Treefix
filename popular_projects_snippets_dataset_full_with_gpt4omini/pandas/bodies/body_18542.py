# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
tz = tz_aware_fixture
tz_didx = date_range("2014-03-01", "2015-01-10", freq="H", tz=tz)
naive_didx = date_range("2014-03-01", "2015-01-10", freq="H")

_compare_utc_to_local(tz_didx)
_compare_local_to_utc(tz_didx, naive_didx)
