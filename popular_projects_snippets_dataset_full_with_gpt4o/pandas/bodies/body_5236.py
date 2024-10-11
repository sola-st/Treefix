# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
td = Timedelta("1 days 02:34:57").as_unit(unit)

res = td.round("min")
assert res == Timedelta("1 days 02:35:00")
assert res._creso == td._creso

res = td.floor("min")
assert res == Timedelta("1 days 02:34:00")
assert res._creso == td._creso

res = td.ceil("min")
assert res == Timedelta("1 days 02:35:00")
assert res._creso == td._creso
