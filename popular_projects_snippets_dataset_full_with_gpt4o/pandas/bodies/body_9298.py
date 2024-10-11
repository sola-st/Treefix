# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
dtype = CategoricalDtype(categories=["a", "b", "c"])
msg = r"codes need to be between -1 and len\(categories\)-1"
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes([-2, 1, 2], categories=dtype.categories)
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes([-2, 1, 2], dtype=dtype)
