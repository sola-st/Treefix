# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
index = MultiIndex.from_tuples([(1, 1), (1, 2), (2, 1)], names=["one", "two"])
obj.index = index
obj_orig = obj.copy()
obj2 = obj.swaplevel()

if using_copy_on_write:
    assert np.shares_memory(obj2.values, obj.values)
else:
    assert not np.shares_memory(obj2.values, obj.values)

obj2.iloc[0] = 0
if using_copy_on_write:
    assert not np.shares_memory(obj2.values, obj.values)
tm.assert_equal(obj, obj_orig)
