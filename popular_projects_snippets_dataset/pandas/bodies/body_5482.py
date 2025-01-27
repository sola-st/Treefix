# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
ts = Timestamp(1_500_000)  # i.e. 1500 microseconds
res = ts.as_unit("ms")

expected = Timestamp(1_000_000)  # i.e. 1 millisecond
assert res == expected

assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value
assert res.value == 1

with pytest.raises(ValueError, match="Cannot losslessly convert units"):
    ts.as_unit("ms", round_ok=False)
