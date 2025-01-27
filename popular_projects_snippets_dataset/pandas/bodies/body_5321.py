# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH 23878
kwds = {kwd_name: 3} if kwd_name is not None else {}
p1_d = "19910905"
p2_d = "19920406"
p1 = Period(p1_d, freq=offset(n, normalize, **kwds))
p2 = Period(p2_d, freq=offset(n, normalize, **kwds))

expected = Period(p2_d, freq=p2.freq.base) - Period(p1_d, freq=p1.freq.base)

assert (p2 - p1) == expected
