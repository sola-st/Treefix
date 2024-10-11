# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
# year, month, day, hour, minute
# second, weekofyear, week, dayofweek, weekday, dayofyear, quarter
# qyear
pi = period_range(freq="A", start="1/1/2001", end="12/1/2005")
self._check_all_fields(pi)

pi = period_range(freq="Q", start="1/1/2001", end="12/1/2002")
self._check_all_fields(pi)

pi = period_range(freq="M", start="1/1/2001", end="1/1/2002")
self._check_all_fields(pi)

pi = period_range(freq="D", start="12/1/2001", end="6/1/2001")
self._check_all_fields(pi)

pi = period_range(freq="B", start="12/1/2001", end="6/1/2001")
self._check_all_fields(pi)

pi = period_range(freq="H", start="12/31/2001", end="1/1/2002 23:00")
self._check_all_fields(pi)

pi = period_range(freq="Min", start="12/31/2001", end="1/1/2002 00:20")
self._check_all_fields(pi)

pi = period_range(
    freq="S", start="12/31/2001 00:00:00", end="12/31/2001 00:05:00"
)
self._check_all_fields(pi)

end_intv = Period("2006-12-31", "W")
i1 = period_range(end=end_intv, periods=10)
self._check_all_fields(i1)
