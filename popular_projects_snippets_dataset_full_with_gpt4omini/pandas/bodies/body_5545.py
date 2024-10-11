# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
msg = "Cannot cast .* to unit='ns' without overflow"
with pytest.raises(ValueError, match=msg):
    Timestamp("1676-01-01").as_unit("ns")
with pytest.raises(ValueError, match=msg):
    Timestamp("2263-01-01").as_unit("ns")

ts = Timestamp("2263-01-01")
assert ts.unit == "s"

ts = Timestamp("1676-01-01")
assert ts.unit == "s"
