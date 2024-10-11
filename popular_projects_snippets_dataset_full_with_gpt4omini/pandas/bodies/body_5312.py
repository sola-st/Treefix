# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("2000-01", "M")

assert (p == zerodim_arr) is expected
assert (zerodim_arr == p) is expected
