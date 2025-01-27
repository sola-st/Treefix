# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
dtype = IntervalDtype("float64", "right")
msg = "Cannot convert .* to .*; subtypes are incompatible"
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)
