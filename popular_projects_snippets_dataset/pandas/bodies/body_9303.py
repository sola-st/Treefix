# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH21767
# float codes should raise even if values are equal to integers
dtype = CategoricalDtype(categories=["a", "b", "c"])

msg = "codes need to be array-like integers"
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes(codes, dtype.categories)
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes(codes, dtype=dtype)
