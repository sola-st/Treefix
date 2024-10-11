# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#13071
p = Period("2011-01", freq="M")
assert p + NaT is NaT
assert NaT + p is NaT
assert p - NaT is NaT
assert NaT - p is NaT
