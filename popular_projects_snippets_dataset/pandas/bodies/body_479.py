# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
with pytest.raises(TypeError, match="A 'tz' is required."):
    DatetimeTZDtype()
