# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# Passing a categorical to a Series and then changing values in either
# the series or the categorical should not change the values in the
# other one, IF you specify copy!
cat = Categorical(["a", "b", "c", "a"])
s = Series(cat, copy=True)
assert s.cat is not cat
s = s.cat.rename_categories([1, 2, 3])
exp_s = np.array([1, 2, 3, 1], dtype=np.int64)
exp_cat = np.array(["a", "b", "c", "a"], dtype=np.object_)
tm.assert_numpy_array_equal(s.__array__(), exp_s)
tm.assert_numpy_array_equal(cat.__array__(), exp_cat)

# setting
s[0] = 2
exp_s2 = np.array([2, 2, 3, 1], dtype=np.int64)
tm.assert_numpy_array_equal(s.__array__(), exp_s2)
tm.assert_numpy_array_equal(cat.__array__(), exp_cat)

# however, copy is False by default
# so this WILL change values
cat = Categorical(["a", "b", "c", "a"])
s = Series(cat)
assert s.values is cat
s = s.cat.rename_categories([1, 2, 3])
assert s.values is not cat
exp_s = np.array([1, 2, 3, 1], dtype=np.int64)
tm.assert_numpy_array_equal(s.__array__(), exp_s)

s[0] = 2
exp_s2 = np.array([2, 2, 3, 1], dtype=np.int64)
tm.assert_numpy_array_equal(s.__array__(), exp_s2)
