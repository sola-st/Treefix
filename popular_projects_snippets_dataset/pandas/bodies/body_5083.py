# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
assert NaT + obj is NaT
assert obj + NaT is NaT
assert NaT - obj is NaT
