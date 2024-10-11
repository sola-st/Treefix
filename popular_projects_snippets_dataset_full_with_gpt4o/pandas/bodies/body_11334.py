# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
# Check that no copy is made when we take all rows in original order
obj_orig = obj.copy()
obj2 = obj.take([0, 1])

if using_copy_on_write:
    assert np.shares_memory(obj2.values, obj.values)
else:
    assert not np.shares_memory(obj2.values, obj.values)

obj2.iloc[0] = 0
if using_copy_on_write:
    assert not np.shares_memory(obj2.values, obj.values)
tm.assert_equal(obj, obj_orig)
