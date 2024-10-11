# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
offset = DateOffset(**{attribute: 0})
msg = "DateOffset objects are immutable"
with pytest.raises(AttributeError, match=msg):
    setattr(offset, attribute, 5)
