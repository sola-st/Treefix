# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("nat", freq="M")
assert repr(NaT) in repr(p)
