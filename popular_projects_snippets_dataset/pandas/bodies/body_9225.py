# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# https://github.com/pandas-dev/pandas/issues/16014
c1 = ctor(["a", "b"], categories=["a", "b"], ordered=False)
c2 = ctor(["a", "b"], categories=["b", "a"], ordered=False)
assert (c1 == c2).all()

c1 = ctor(["a", "b"], categories=["a", "b"], ordered=False)
c2 = ctor(["b", "a"], categories=["b", "a"], ordered=False)
assert (c1 != c2).all()

c1 = ctor(["a", "a"], categories=["a", "b"], ordered=False)
c2 = ctor(["b", "b"], categories=["b", "a"], ordered=False)
assert (c1 != c2).all()

c1 = ctor(["a", "a"], categories=["a", "b"], ordered=False)
c2 = ctor(["a", "b"], categories=["b", "a"], ordered=False)
result = c1 == c2
tm.assert_numpy_array_equal(np.array(result), np.array([True, False]))
