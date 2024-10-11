# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
result = factor[factor == "a"]
expected = factor[np.asarray(factor) == "a"]
tm.assert_categorical_equal(result, expected)

result = factor[factor != "a"]
expected = factor[np.asarray(factor) != "a"]
tm.assert_categorical_equal(result, expected)

result = factor[factor < "c"]
expected = factor[np.asarray(factor) < "c"]
tm.assert_categorical_equal(result, expected)

result = factor[factor > "a"]
expected = factor[np.asarray(factor) > "a"]
tm.assert_categorical_equal(result, expected)

result = factor[factor >= "b"]
expected = factor[np.asarray(factor) >= "b"]
tm.assert_categorical_equal(result, expected)

result = factor[factor <= "b"]
expected = factor[np.asarray(factor) <= "b"]
tm.assert_categorical_equal(result, expected)

n = len(factor)

other = factor[np.random.permutation(n)]
result = factor == other
expected = np.asarray(factor) == np.asarray(other)
tm.assert_numpy_array_equal(result, expected)

result = factor == "d"
expected = np.zeros(len(factor), dtype=bool)
tm.assert_numpy_array_equal(result, expected)

# comparisons with categoricals
cat_rev = Categorical(["a", "b", "c"], categories=["c", "b", "a"], ordered=True)
cat_rev_base = Categorical(
    ["b", "b", "b"], categories=["c", "b", "a"], ordered=True
)
cat = Categorical(["a", "b", "c"], ordered=True)
cat_base = Categorical(["b", "b", "b"], categories=cat.categories, ordered=True)

# comparisons need to take categories ordering into account
res_rev = cat_rev > cat_rev_base
exp_rev = np.array([True, False, False])
tm.assert_numpy_array_equal(res_rev, exp_rev)

res_rev = cat_rev < cat_rev_base
exp_rev = np.array([False, False, True])
tm.assert_numpy_array_equal(res_rev, exp_rev)

res = cat > cat_base
exp = np.array([False, False, True])
tm.assert_numpy_array_equal(res, exp)

# Only categories with same categories can be compared
msg = "Categoricals can only be compared if 'categories' are the same"
with pytest.raises(TypeError, match=msg):
    cat > cat_rev

cat_rev_base2 = Categorical(["b", "b", "b"], categories=["c", "b", "a", "d"])

with pytest.raises(TypeError, match=msg):
    cat_rev > cat_rev_base2

# Only categories with same ordering information can be compared
cat_unorderd = cat.set_ordered(False)
assert not (cat > cat).any()

with pytest.raises(TypeError, match=msg):
    cat > cat_unorderd

# comparison (in both directions) with Series will raise
s = Series(["b", "b", "b"])
msg = (
    "Cannot compare a Categorical for op __gt__ with type "
    r"<class 'numpy\.ndarray'>"
)
with pytest.raises(TypeError, match=msg):
    cat > s
with pytest.raises(TypeError, match=msg):
    cat_rev > s
with pytest.raises(TypeError, match=msg):
    s < cat
with pytest.raises(TypeError, match=msg):
    s < cat_rev

# comparison with numpy.array will raise in both direction, but only on
# newer numpy versions
a = np.array(["b", "b", "b"])
with pytest.raises(TypeError, match=msg):
    cat > a
with pytest.raises(TypeError, match=msg):
    cat_rev > a

# Make sure that unequal comparison take the categories order in
# account
cat_rev = Categorical(list("abc"), categories=list("cba"), ordered=True)
exp = np.array([True, False, False])
res = cat_rev > "b"
tm.assert_numpy_array_equal(res, exp)

# check that zero-dim array gets unboxed
res = cat_rev > np.array("b")
tm.assert_numpy_array_equal(res, exp)
