# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py

exp_arr = np.array(["a", "b", "c", "a", "b", "c"], dtype=np.object_)
c1 = Categorical(exp_arr)
tm.assert_numpy_array_equal(c1.__array__(), exp_arr)
c2 = Categorical(exp_arr, categories=["a", "b", "c"])
tm.assert_numpy_array_equal(c2.__array__(), exp_arr)
c2 = Categorical(exp_arr, categories=["c", "b", "a"])
tm.assert_numpy_array_equal(c2.__array__(), exp_arr)

# categories must be unique
msg = "Categorical categories must be unique"
with pytest.raises(ValueError, match=msg):
    Categorical([1, 2], [1, 2, 2])

with pytest.raises(ValueError, match=msg):
    Categorical(["a", "b"], ["a", "b", "b"])

# The default should be unordered
c1 = Categorical(["a", "b", "c", "a"])
assert not c1.ordered

# Categorical as input
c1 = Categorical(["a", "b", "c", "a"])
c2 = Categorical(c1)
tm.assert_categorical_equal(c1, c2)

c1 = Categorical(["a", "b", "c", "a"], categories=["a", "b", "c", "d"])
c2 = Categorical(c1)
tm.assert_categorical_equal(c1, c2)

c1 = Categorical(["a", "b", "c", "a"], categories=["a", "c", "b"])
c2 = Categorical(c1)
tm.assert_categorical_equal(c1, c2)

c1 = Categorical(["a", "b", "c", "a"], categories=["a", "c", "b"])
c2 = Categorical(c1, categories=["a", "b", "c"])
tm.assert_numpy_array_equal(c1.__array__(), c2.__array__())
tm.assert_index_equal(c2.categories, Index(["a", "b", "c"]))

# Series of dtype category
c1 = Categorical(["a", "b", "c", "a"], categories=["a", "b", "c", "d"])
c2 = Categorical(Series(c1))
tm.assert_categorical_equal(c1, c2)

c1 = Categorical(["a", "b", "c", "a"], categories=["a", "c", "b"])
c2 = Categorical(Series(c1))
tm.assert_categorical_equal(c1, c2)

# Series
c1 = Categorical(["a", "b", "c", "a"])
c2 = Categorical(Series(["a", "b", "c", "a"]))
tm.assert_categorical_equal(c1, c2)

c1 = Categorical(["a", "b", "c", "a"], categories=["a", "b", "c", "d"])
c2 = Categorical(Series(["a", "b", "c", "a"]), categories=["a", "b", "c", "d"])
tm.assert_categorical_equal(c1, c2)

# This should result in integer categories, not float!
cat = Categorical([1, 2, 3, np.nan], categories=[1, 2, 3])
assert is_integer_dtype(cat.categories)

# https://github.com/pandas-dev/pandas/issues/3678
cat = Categorical([np.nan, 1, 2, 3])
assert is_integer_dtype(cat.categories)

# this should result in floats
cat = Categorical([np.nan, 1, 2.0, 3])
assert is_float_dtype(cat.categories)

cat = Categorical([np.nan, 1.0, 2.0, 3.0])
assert is_float_dtype(cat.categories)

# This doesn't work -> this would probably need some kind of "remember
# the original type" feature to try to cast the array interface result
# to...

# vals = np.asarray(cat[cat.notna()])
# assert is_integer_dtype(vals)

# corner cases
cat = Categorical([1])
assert len(cat.categories) == 1
assert cat.categories[0] == 1
assert len(cat.codes) == 1
assert cat.codes[0] == 0

cat = Categorical(["a"])
assert len(cat.categories) == 1
assert cat.categories[0] == "a"
assert len(cat.codes) == 1
assert cat.codes[0] == 0

# two arrays
#  - when the first is an integer dtype and the second is not
#  - when the resulting codes are all -1/NaN
with tm.assert_produces_warning(None):
    Categorical([0, 1, 2, 0, 1, 2], categories=["a", "b", "c"])

with tm.assert_produces_warning(None):
    Categorical([0, 1, 2, 0, 1, 2], categories=[3, 4, 5])

# the next one are from the old docs
with tm.assert_produces_warning(None):
    Categorical([0, 1, 2, 0, 1, 2], [1, 2, 3])
    cat = Categorical([1, 2], categories=[1, 2, 3])

# this is a legitimate constructor
with tm.assert_produces_warning(None):
    Categorical(np.array([], dtype="int64"), categories=[3, 2, 1], ordered=True)
