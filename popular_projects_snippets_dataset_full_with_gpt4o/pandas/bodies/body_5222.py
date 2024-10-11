# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py

for td in [Timedelta(10, unit="d"), Timedelta("1 days, 10:11:12.012345")]:
    pydt = td.to_pytimedelta()
    assert td == Timedelta(pydt)
    assert td == pydt
    assert isinstance(pydt, timedelta) and not isinstance(pydt, Timedelta)

    assert td == np.timedelta64(td.value, "ns")
    td64 = td.to_timedelta64()

    assert td64 == np.timedelta64(td.value, "ns")
    assert td == td64

    assert isinstance(td64, np.timedelta64)

# this is NOT equal and cannot be roundtripped (because of the nanos)
td = Timedelta("1 days, 10:11:12.012345678")
assert td != td.to_pytimedelta()
