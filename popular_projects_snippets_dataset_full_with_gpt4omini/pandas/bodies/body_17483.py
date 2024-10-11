# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
cls = offset_types
with pytest.raises(ValueError, match="argument must be an integer"):
    cls(n=1.5)
