# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# microsecond that would be just out of bounds for nano
us = 9223372800000000
td = Timedelta._from_value_and_reso(us, NpyDatetimeUnit.NPY_FR_us.value)

msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td.as_unit("ns")

res = td.as_unit("ms")
assert res.value == us // 1000
assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value
