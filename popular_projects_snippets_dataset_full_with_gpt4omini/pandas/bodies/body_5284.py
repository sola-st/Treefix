# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period(ordinal=-1, freq="Q-DEC")
assert p.year == 1969
assert p.quarter == 4
assert isinstance(p, Period)

p = Period(ordinal=-2, freq="Q-DEC")
assert p.year == 1969
assert p.quarter == 3
assert isinstance(p, Period)

p = Period(ordinal=-2, freq="M")
assert p.year == 1969
assert p.month == 11
assert isinstance(p, Period)
