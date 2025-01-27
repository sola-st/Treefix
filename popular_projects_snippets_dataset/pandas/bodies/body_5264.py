# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("2011-01", freq="M")
res = Period._from_ordinal(p.ordinal, freq="M")
assert p == res
assert isinstance(res, Period)
