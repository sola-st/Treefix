# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# https://github.com/pandas-dev/pandas/issues/8420
# https://github.com/pandas-dev/pandas/issues/14522

cat = Categorical(
    ["cheese", "milk", "apple", "bread", "bread"],
    categories=["cheese", "milk", "apple", "bread"],
    ordered=ordered,
)
ser = Series(cat)

# Searching for single item argument, side='left' (default)
res_cat = cat.searchsorted("apple")
assert res_cat == 2
assert is_scalar(res_cat)

res_ser = ser.searchsorted("apple")
assert res_ser == 2
assert is_scalar(res_ser)

# Searching for single item array, side='left' (default)
res_cat = cat.searchsorted(["bread"])
res_ser = ser.searchsorted(["bread"])
exp = np.array([3], dtype=np.intp)
tm.assert_numpy_array_equal(res_cat, exp)
tm.assert_numpy_array_equal(res_ser, exp)

# Searching for several items array, side='right'
res_cat = cat.searchsorted(["apple", "bread"], side="right")
res_ser = ser.searchsorted(["apple", "bread"], side="right")
exp = np.array([3, 5], dtype=np.intp)
tm.assert_numpy_array_equal(res_cat, exp)
tm.assert_numpy_array_equal(res_ser, exp)

# Searching for a single value that is not from the Categorical
with pytest.raises(TypeError, match="cucumber"):
    cat.searchsorted("cucumber")
with pytest.raises(TypeError, match="cucumber"):
    ser.searchsorted("cucumber")

# Searching for multiple values one of each is not from the Categorical
msg = (
    "Cannot setitem on a Categorical with a new category, "
    "set the categories first"
)
with pytest.raises(TypeError, match=msg):
    cat.searchsorted(["bread", "cucumber"])
with pytest.raises(TypeError, match=msg):
    ser.searchsorted(["bread", "cucumber"])
