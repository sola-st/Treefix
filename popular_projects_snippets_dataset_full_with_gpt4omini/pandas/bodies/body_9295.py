# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
dtype = CategoricalDtype(categories=[1, 2])
msg = "codes need to be array-like integers"
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes(["a"], categories=dtype.categories)
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes(["a"], dtype=dtype)
