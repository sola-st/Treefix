# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
obj.index = Index([Timestamp("2019-12-31"), Timestamp("2020-12-31")])

obj_orig = obj.copy()
obj2 = obj.to_period(freq="Y")

if using_copy_on_write:
    assert np.shares_memory(get_array(obj2, "a"), get_array(obj, "a"))
else:
    assert not np.shares_memory(get_array(obj2, "a"), get_array(obj, "a"))

# mutating obj2 triggers a copy-on-write for that column / block
obj2.iloc[0] = 0
assert not np.shares_memory(get_array(obj2, "a"), get_array(obj, "a"))
tm.assert_equal(obj, obj_orig)
