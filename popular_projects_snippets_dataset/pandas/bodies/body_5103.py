# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
result = NaT - td
assert result is NaT

result = np.datetime64("NaT") - td
assert result is NaT
