# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_constructors.py
# Case: constructing a Series from another Series object follows CoW rules:
# a new object is returned and thus mutations are not propagated
ser = Series([1, 2, 3], name="name")

# default is copy=False -> new Series is a shallow copy / view of original
result = Series(ser)

# the shallow copy still shares memory
assert np.shares_memory(ser.values, result.values)

if using_copy_on_write:
    assert result._mgr.refs is not None

if using_copy_on_write:
    # mutating new series copy doesn't mutate original
    result.iloc[0] = 0
    assert ser.iloc[0] == 1
    # mutating triggered a copy-on-write -> no longer shares memory
    assert not np.shares_memory(ser.values, result.values)
else:
    # mutating shallow copy does mutate original
    result.iloc[0] = 0
    assert ser.iloc[0] == 0
    # and still shares memory
    assert np.shares_memory(ser.values, result.values)

# the same when modifying the parent
result = Series(ser)

if using_copy_on_write:
    # mutating original doesn't mutate new series
    ser.iloc[0] = 0
    assert result.iloc[0] == 1
else:
    # mutating original does mutate shallow copy
    ser.iloc[0] = 0
    assert result.iloc[0] == 0
