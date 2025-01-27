# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py

# invalid accessor
msg = r"Can only use \.cat accessor with a 'category' dtype"
with pytest.raises(AttributeError, match=msg):
    Series([1, 2, 3]).cat
with pytest.raises(AttributeError, match=msg):
    Series([1, 2, 3]).cat()
with pytest.raises(AttributeError, match=msg):
    Series(["a", "b", "c"]).cat
with pytest.raises(AttributeError, match=msg):
    Series(np.arange(5.0)).cat
with pytest.raises(AttributeError, match=msg):
    Series([Timestamp("20130101")]).cat

# Series should delegate calls to '.categories', '.codes', '.ordered'
# and the methods '.set_categories()' 'drop_unused_categories()' to the
# categorical
ser = Series(Categorical(["a", "b", "c", "a"], ordered=True))
exp_categories = Index(["a", "b", "c"])
tm.assert_index_equal(ser.cat.categories, exp_categories)
ser = ser.cat.rename_categories([1, 2, 3])
exp_categories = Index([1, 2, 3])
tm.assert_index_equal(ser.cat.categories, exp_categories)

exp_codes = Series([0, 1, 2, 0], dtype="int8")
tm.assert_series_equal(ser.cat.codes, exp_codes)

assert ser.cat.ordered
ser = ser.cat.as_unordered()
assert not ser.cat.ordered

ser = ser.cat.as_ordered()
assert ser.cat.ordered

# reorder
ser = Series(Categorical(["a", "b", "c", "a"], ordered=True))
exp_categories = Index(["c", "b", "a"])
exp_values = np.array(["a", "b", "c", "a"], dtype=np.object_)
ser = ser.cat.set_categories(["c", "b", "a"])
tm.assert_index_equal(ser.cat.categories, exp_categories)
tm.assert_numpy_array_equal(ser.values.__array__(), exp_values)
tm.assert_numpy_array_equal(ser.__array__(), exp_values)

# remove unused categories
ser = Series(Categorical(["a", "b", "b", "a"], categories=["a", "b", "c"]))
exp_categories = Index(["a", "b"])
exp_values = np.array(["a", "b", "b", "a"], dtype=np.object_)
ser = ser.cat.remove_unused_categories()
tm.assert_index_equal(ser.cat.categories, exp_categories)
tm.assert_numpy_array_equal(ser.values.__array__(), exp_values)
tm.assert_numpy_array_equal(ser.__array__(), exp_values)

# This method is likely to be confused, so test that it raises an error
# on wrong inputs:
msg = "'Series' object has no attribute 'set_categories'"
with pytest.raises(AttributeError, match=msg):
    ser.set_categories([4, 3, 2, 1])

# right: ser.cat.set_categories([4,3,2,1])

# GH#18862 (let Series.cat.rename_categories take callables)
ser = Series(Categorical(["a", "b", "c", "a"], ordered=True))
result = ser.cat.rename_categories(lambda x: x.upper())
expected = Series(
    Categorical(["A", "B", "C", "A"], categories=["A", "B", "C"], ordered=True)
)
tm.assert_series_equal(result, expected)
