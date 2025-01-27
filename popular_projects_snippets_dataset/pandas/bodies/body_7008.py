# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_equals.py
ci1 = CategoricalIndex(["a", "b"], categories=["a", "b"], ordered=True)
ci2 = CategoricalIndex(["a", "b"], categories=["a", "b", "c"], ordered=True)

assert ci1.equals(ci1)
assert not ci1.equals(ci2)
assert ci1.equals(ci1.astype(object))
assert ci1.astype(object).equals(ci1)

assert (ci1 == ci1).all()
assert not (ci1 != ci1).all()
assert not (ci1 > ci1).all()
assert not (ci1 < ci1).all()
assert (ci1 <= ci1).all()
assert (ci1 >= ci1).all()

assert not (ci1 == 1).all()
assert (ci1 == Index(["a", "b"])).all()
assert (ci1 == ci1.values).all()

# invalid comparisons
with pytest.raises(ValueError, match="Lengths must match"):
    ci1 == Index(["a", "b", "c"])

msg = "Categoricals can only be compared if 'categories' are the same"
with pytest.raises(TypeError, match=msg):
    ci1 == ci2
with pytest.raises(TypeError, match=msg):
    ci1 == Categorical(ci1.values, ordered=False)
with pytest.raises(TypeError, match=msg):
    ci1 == Categorical(ci1.values, categories=list("abc"))

# tests
# make sure that we are testing for category inclusion properly
ci = CategoricalIndex(list("aabca"), categories=["c", "a", "b"])
assert not ci.equals(list("aabca"))
# Same categories, but different order
# Unordered
assert ci.equals(CategoricalIndex(list("aabca")))
# Ordered
assert not ci.equals(CategoricalIndex(list("aabca"), ordered=True))
assert ci.equals(ci.copy())

ci = CategoricalIndex(list("aabca") + [np.nan], categories=["c", "a", "b"])
assert not ci.equals(list("aabca"))
assert not ci.equals(CategoricalIndex(list("aabca")))
assert ci.equals(ci.copy())

ci = CategoricalIndex(list("aabca") + [np.nan], categories=["c", "a", "b"])
assert not ci.equals(list("aabca") + [np.nan])
assert ci.equals(CategoricalIndex(list("aabca") + [np.nan]))
assert not ci.equals(CategoricalIndex(list("aabca") + [np.nan], ordered=True))
assert ci.equals(ci.copy())
