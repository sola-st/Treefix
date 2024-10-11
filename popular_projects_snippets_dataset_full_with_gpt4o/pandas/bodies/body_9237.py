# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# Gh-24142
target = Categorical(["a", "b"], categories=["a", "b"], ordered=True)
mask = np.array([True, False])
msg = "Cannot set a Categorical with another, without identical categories"
with pytest.raises(TypeError, match=msg):
    target[mask] = other[mask]
