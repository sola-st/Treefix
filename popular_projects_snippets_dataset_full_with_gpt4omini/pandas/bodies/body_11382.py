# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_constructors.py
# Case: constructing a Series from another Series with specifying an index
# that potentially requires a reindex of the values
ser = Series([1, 2, 3], name="name")

# passing an index that doesn't actually require a reindex of the values
# -> without CoW we get an actual mutating view
for index in [
    ser.index,
    ser.index.copy(),
    list(ser.index),
    ser.index.rename("idx"),
]:
    result = Series(ser, index=index)
    assert np.shares_memory(ser.values, result.values)
    result.iloc[0] = 0
    if using_copy_on_write:
        assert ser.iloc[0] == 1
    else:
        assert ser.iloc[0] == 0

    # ensure that if an actual reindex is needed, we don't have any refs
    # (mutating the result wouldn't trigger CoW)
result = Series(ser, index=[0, 1, 2, 3])
assert not np.shares_memory(ser.values, result.values)
if using_copy_on_write:
    assert result._mgr.refs is None or result._mgr.refs[0] is None
