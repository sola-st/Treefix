# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
dtype = CategoricalDtype(categories=[1, 2])
msg = "codes need to be between "
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes([1, 2], categories=dtype.categories)
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes([1, 2], dtype=dtype)
