# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(days=2, hours=6)

result = divmod(td, timedelta(days=1))
assert result[0] == 2
assert isinstance(result[1], Timedelta)
assert result[1] == Timedelta(hours=6)

result = divmod(td, 54)
assert result[0] == Timedelta(hours=1)
assert isinstance(result[1], Timedelta)
assert result[1] == Timedelta(0)

result = divmod(td, NaT)
assert np.isnan(result[0])
assert result[1] is NaT
