# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(hours=37)

result = td % np.timedelta64("NaT", "ns")
assert result is NaT
