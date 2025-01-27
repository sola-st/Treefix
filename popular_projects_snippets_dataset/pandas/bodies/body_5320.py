# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH 23878
p1 = Period("19910905", freq=tick_classes(n))
p2 = Period("19920406", freq=tick_classes(n))

expected = Period(str(p2), freq=p2.freq.base) - Period(
    str(p1), freq=p1.freq.base
)

assert (p2 - p1) == expected
