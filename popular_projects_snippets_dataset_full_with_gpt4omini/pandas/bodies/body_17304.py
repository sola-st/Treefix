# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py

# GH 4633
# look at the boolean/nonzero behavior for objects
obj = construct(frame_or_series, shape=4)
msg = f"The truth value of a {frame_or_series.__name__} is ambiguous"
with pytest.raises(ValueError, match=msg):
    bool(obj == 0)
with pytest.raises(ValueError, match=msg):
    bool(obj == 1)
with pytest.raises(ValueError, match=msg):
    bool(obj)

obj = construct(frame_or_series, shape=4, value=1)
with pytest.raises(ValueError, match=msg):
    bool(obj == 0)
with pytest.raises(ValueError, match=msg):
    bool(obj == 1)
with pytest.raises(ValueError, match=msg):
    bool(obj)

obj = construct(frame_or_series, shape=4, value=np.nan)
with pytest.raises(ValueError, match=msg):
    bool(obj == 0)
with pytest.raises(ValueError, match=msg):
    bool(obj == 1)
with pytest.raises(ValueError, match=msg):
    bool(obj)

# empty
obj = construct(frame_or_series, shape=0)
with pytest.raises(ValueError, match=msg):
    bool(obj)

# invalid behaviors

obj1 = construct(frame_or_series, shape=4, value=1)
obj2 = construct(frame_or_series, shape=4, value=1)

with pytest.raises(ValueError, match=msg):
    if obj1:
        pass

with pytest.raises(ValueError, match=msg):
    obj1 and obj2
with pytest.raises(ValueError, match=msg):
    obj1 or obj2
with pytest.raises(ValueError, match=msg):
    not obj1
