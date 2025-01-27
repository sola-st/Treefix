# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
cat_rev = Series(Categorical(data, categories=reverse, ordered=True))
cat_rev_base = Series(Categorical(base, categories=reverse, ordered=True))
cat = Series(Categorical(data, ordered=True))
cat_base = Series(
    Categorical(base, categories=cat.cat.categories, ordered=True)
)
s = Series(base)
a = np.array(base)

# comparisons need to take categories ordering into account
res_rev = cat_rev > cat_rev_base
exp_rev = Series([True, False, False])
tm.assert_series_equal(res_rev, exp_rev)

res_rev = cat_rev < cat_rev_base
exp_rev = Series([False, False, True])
tm.assert_series_equal(res_rev, exp_rev)

res = cat > cat_base
exp = Series([False, False, True])
tm.assert_series_equal(res, exp)

scalar = base[1]
res = cat > scalar
exp = Series([False, False, True])
exp2 = cat.values > scalar
tm.assert_series_equal(res, exp)
tm.assert_numpy_array_equal(res.values, exp2)
res_rev = cat_rev > scalar
exp_rev = Series([True, False, False])
exp_rev2 = cat_rev.values > scalar
tm.assert_series_equal(res_rev, exp_rev)
tm.assert_numpy_array_equal(res_rev.values, exp_rev2)

# Only categories with same categories can be compared
msg = "Categoricals can only be compared if 'categories' are the same"
with pytest.raises(TypeError, match=msg):
    cat > cat_rev

# categorical cannot be compared to Series or numpy array, and also
# not the other way around
msg = (
    "Cannot compare a Categorical for op __gt__ with type "
    r"<class 'numpy\.ndarray'>"
)
with pytest.raises(TypeError, match=msg):
    cat > s
with pytest.raises(TypeError, match=msg):
    cat_rev > s
with pytest.raises(TypeError, match=msg):
    cat > a
with pytest.raises(TypeError, match=msg):
    cat_rev > a

with pytest.raises(TypeError, match=msg):
    s < cat
with pytest.raises(TypeError, match=msg):
    s < cat_rev

with pytest.raises(TypeError, match=msg):
    a < cat
with pytest.raises(TypeError, match=msg):
    a < cat_rev
