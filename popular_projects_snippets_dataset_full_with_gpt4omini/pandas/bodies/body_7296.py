# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta_range.py
# GH 33498 only the cases where `(end % freq) == 0` used to fail
res = timedelta_range(start=start, end=end, freq=freq)
assert Timedelta(start) == res[0]
assert Timedelta(end) >= res[-1]
assert len(res) == expected_periods
