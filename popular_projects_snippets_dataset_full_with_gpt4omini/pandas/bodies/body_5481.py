# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# microsecond that would be just out of bounds for nano
us = 9223372800000000
ts = Timestamp._from_value_and_reso(us, NpyDatetimeUnit.NPY_FR_us.value, None)

msg = "Cannot cast 2262-04-12 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    ts.as_unit("ns")

res = ts.as_unit("ms")
assert res.value == us // 1000
assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value
