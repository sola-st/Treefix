# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#47267 avoid the conversions in cast_from-unit

msg = "Conversion of non-round float with unit=[MY] is ambiguous"
with pytest.raises(ValueError, match=msg):
    Timestamp(150.5, unit="Y")

with pytest.raises(ValueError, match=msg):
    Timestamp(150.5, unit="M")
