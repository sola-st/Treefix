# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# GH-24142
target = Categorical(["a", "b"], categories=["a", "b"])
mask = np.array([True, False])
target[mask] = other[mask]
expected = Categorical(["b", "b"], categories=["a", "b"])
tm.assert_categorical_equal(target, expected)
