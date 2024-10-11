# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_common.py
off = offset2
msg = "Cannot subtract datetime from offset"
with pytest.raises(TypeError, match=msg):
    off - date

assert 2 * off - off == off
assert date - offset2 == date + offset_box(-2)
assert date - offset2 == date - (2 * off - off)
