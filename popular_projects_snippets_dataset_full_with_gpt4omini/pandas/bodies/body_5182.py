# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# TODO: parametrize over units just above/below the implementation bounds
#  once GH#38964 is resolved

# Timedelta.max is just under 106752 days
td64 = np.timedelta64(val, unit)
assert td64.astype("m8[ns]").view("i8") < 0  # i.e. naive astype will be wrong

td = Timedelta(td64)
if unit != "M":
    # with unit="M" the conversion to "s" is poorly defined
    #  (and numpy issues DeprecationWarning)
    assert td.asm8 == td64
assert td.asm8.dtype == "m8[s]"
msg = r"Cannot cast 1067\d\d days .* to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td.as_unit("ns")

# But just back in bounds and we are OK
assert Timedelta(td64 - 1) == td64 - 1

td64 *= -1
assert td64.astype("m8[ns]").view("i8") > 0  # i.e. naive astype will be wrong

td2 = Timedelta(td64)
msg = r"Cannot cast -1067\d\d days .* to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td2.as_unit("ns")

# But just back in bounds and we are OK
assert Timedelta(td64 + 1) == td64 + 1
