# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# np.float64('NaN') has a 'dtype' attr, avoid treating as array
td = Timedelta(10, unit="d")
result = op(td, nan)
assert result is NaT
