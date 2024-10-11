# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
per = Period("2011-01", freq=freq)

# For subtraction, NaT is treated as another Period object
assert NaT - per is NaT
assert per - NaT is NaT

# For addition, NaT is treated as offset-like
assert NaT + per is NaT
assert per + NaT is NaT
