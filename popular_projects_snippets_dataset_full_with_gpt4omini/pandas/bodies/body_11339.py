# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
obj_orig = obj.copy()
view = obj[:]
obj.sort_values(inplace=True, **kwargs)

assert np.shares_memory(get_array(obj, "a"), get_array(view, "a"))

# mutating obj triggers a copy-on-write for the column / block
obj.iloc[0] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(obj, "a"), get_array(view, "a"))
    tm.assert_equal(view, obj_orig)
else:
    assert np.shares_memory(get_array(obj, "a"), get_array(view, "a"))
