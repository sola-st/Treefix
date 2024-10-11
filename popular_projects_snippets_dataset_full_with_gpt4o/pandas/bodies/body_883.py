# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
block = create_block("datetime", [0])

assert block._can_hold_element([])

# We will check that block._can_hold_element iff arr.__setitem__ works
arr = pd.array(block.values.ravel())

# coerce None
assert block._can_hold_element(None)
arr[0] = None
assert arr[0] is pd.NaT

# coerce different types of datetime objects
vals = [np.datetime64("2010-10-10"), datetime(2010, 10, 10)]
for val in vals:
    assert block._can_hold_element(val)
    arr[0] = val

val = date(2010, 10, 10)
assert not block._can_hold_element(val)

msg = (
    "value should be a 'Timestamp', 'NaT', "
    "or array of those. Got 'date' instead."
)
with pytest.raises(TypeError, match=msg):
    arr[0] = val
