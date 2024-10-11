# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#47266 avoid the conversions in cast_from_unit
val = typ(150)

ts = Timestamp(val, unit="Y")
expected = Timestamp("2120-01-01")
assert ts == expected

ts = Timestamp(val, unit="M")
expected = Timestamp("1982-07-01")
assert ts == expected
