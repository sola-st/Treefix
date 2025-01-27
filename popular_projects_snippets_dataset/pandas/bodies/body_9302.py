# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH21767
codes = [1, 2, np.nan]
dtype = CategoricalDtype(categories=["a", "b", "c"])
with pytest.raises(ValueError, match="codes need to be array-like integers"):
    Categorical.from_codes(codes, categories=dtype.categories)
with pytest.raises(ValueError, match="codes need to be array-like integers"):
    Categorical.from_codes(codes, dtype=dtype)
