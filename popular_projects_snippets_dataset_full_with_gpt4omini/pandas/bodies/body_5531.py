# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
msg = "Cannot convert input"
with pytest.raises(TypeError, match=msg):
    Timestamp(slice(2))
msg = "Cannot convert Period"
with pytest.raises(ValueError, match=msg):
    Timestamp(Period("1000-01-01"))
