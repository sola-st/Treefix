# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
msg = "boolean value of NA is ambiguous"

with pytest.raises(TypeError, match=msg):
    bool(NA)

with pytest.raises(TypeError, match=msg):
    not NA
