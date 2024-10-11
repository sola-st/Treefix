# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
# float64 -> uint64 fails with negative values
index = interval_range(-10.0, 10.0)
dtype = IntervalDtype("uint64", "right")
msg = re.escape(
    "Cannot convert interval[float64, right] to interval[uint64, right]; "
    "subtypes are incompatible"
)
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)
