# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH 19016
msg = (
    "category, object, and string subtypes are not supported "
    "for IntervalDtype"
)
with pytest.raises(TypeError, match=msg):
    IntervalDtype(subtype)
