# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#9416
obj = frame_or_series(["a", "b", "c", "d"], dtype="category")

rt = obj.shift(1).shift(-1)
tm.assert_equal(obj.iloc[:-1], rt.dropna())

def get_cat_values(ndframe):
    # For Series we could just do ._values; for DataFrame
    #  we may be able to do this if we ever have 2D Categoricals
    exit(ndframe._mgr.arrays[0])

cat = get_cat_values(obj)

sp1 = obj.shift(1)
tm.assert_index_equal(obj.index, sp1.index)
assert np.all(get_cat_values(sp1).codes[:1] == -1)
assert np.all(cat.codes[:-1] == get_cat_values(sp1).codes[1:])

sn2 = obj.shift(-2)
tm.assert_index_equal(obj.index, sn2.index)
assert np.all(get_cat_values(sn2).codes[-2:] == -1)
assert np.all(cat.codes[2:] == get_cat_values(sn2).codes[:-2])

tm.assert_index_equal(cat.categories, get_cat_values(sp1).categories)
tm.assert_index_equal(cat.categories, get_cat_values(sn2).categories)
