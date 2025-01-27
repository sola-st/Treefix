# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# GH#3374
value = Timedelta("1day").value * 20169940
msg = "Cannot cast 1742682816000000000000 from ns to 'ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(value)

# xref GH#17637
msg = "Cannot cast 139993 from D to 'ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(7 * 19999, unit="D")

# used to overflow before non-ns support
td = Timedelta(timedelta(days=13 * 19999))
assert td._creso == NpyDatetimeUnit.NPY_FR_us.value
assert td.days == 13 * 19999
