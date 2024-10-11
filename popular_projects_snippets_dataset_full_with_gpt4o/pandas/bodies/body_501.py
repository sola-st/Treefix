# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "could not construct IntervalDtype"
with pytest.raises(TypeError, match=msg):
    IntervalDtype(subtype)
