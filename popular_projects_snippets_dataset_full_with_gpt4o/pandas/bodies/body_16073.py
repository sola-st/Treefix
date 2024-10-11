# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
ser = Series(Categorical(["a", "b", np.nan, "a"]))
tm.assert_index_equal(ser.cat.categories, Index(["a", "b"]))
assert not ser.cat.ordered, False

exp = Categorical(["a", "b", np.nan, "a"], categories=["b", "a"])

res = ser.cat.set_categories(["b", "a"])
tm.assert_categorical_equal(res.values, exp)

ser[:] = "a"
ser = ser.cat.remove_unused_categories()
tm.assert_index_equal(ser.cat.categories, Index(["a"]))
