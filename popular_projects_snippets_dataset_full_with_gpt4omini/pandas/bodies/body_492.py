# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
dt = PeriodDtype()
msg = "object has no attribute 'freqstr'"
with pytest.raises(AttributeError, match=msg):
    str(dt)
