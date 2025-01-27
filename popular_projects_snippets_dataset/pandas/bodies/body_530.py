# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
with pytest.raises(TypeError, match="ordered"):
    CategoricalDtype(["a", "b"], ordered="foo")

with pytest.raises(TypeError, match="'categories' must be list-like"):
    CategoricalDtype("category")
