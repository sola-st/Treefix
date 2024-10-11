# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
expected = Period("2007-01", freq="2M")
assert Period(year=2007, month=1, freq="2M") == expected

assert Period(None) is NaT

p = Period("2007-01-01", freq="D")

result = Period(p, freq="A")
exp = Period("2007", freq="A")
assert result == exp
