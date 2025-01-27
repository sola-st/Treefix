# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH#21341 check that __setattr__ raises
offset = _create_offset(offset_types)
msg = "objects is not writable|DateOffset objects are immutable"
with pytest.raises(AttributeError, match=msg):
    offset.normalize = True
with pytest.raises(AttributeError, match=msg):
    offset.n = 91
