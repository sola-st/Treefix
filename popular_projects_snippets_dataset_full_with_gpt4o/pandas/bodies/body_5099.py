# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
td_nat = np.timedelta64("NaT")

result = td - td_nat
assert result is NaT

result = td_nat - td
assert result is NaT
