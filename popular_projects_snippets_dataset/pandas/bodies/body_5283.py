# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH 13727
p = Period("2000-01-01 00:00:00", freq=freq)
assert p.is_leap_year
assert isinstance(p.is_leap_year, bool)

p = Period("1999-01-01 00:00:00", freq=freq)
assert not p.is_leap_year

p = Period("2004-01-01 00:00:00", freq=freq)
assert p.is_leap_year

p = Period("2100-01-01 00:00:00", freq=freq)
assert not p.is_leap_year
