# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
td64 = np.timedelta64(val, unit)
with pytest.raises(OutOfBoundsTimedelta, match=str(td64)):
    Timedelta(td64)

# But just back in bounds and we are OK
assert Timedelta(td64 - 10**9) == td64 - 10**9
