# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
off = offset2
msg = "Cannot subtract datetime from offset"
with pytest.raises(TypeError, match=msg):
    off - dt
assert 2 * off - off == off

assert dt - offset2 == dt + _offset(-3)
