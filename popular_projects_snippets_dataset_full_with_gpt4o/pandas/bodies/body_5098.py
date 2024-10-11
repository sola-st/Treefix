# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# In this context pd.NaT is treated as timedelta-like
td = Timedelta(10, unit="d")
result = td - NaT
assert result is NaT
