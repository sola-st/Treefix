# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "Parameter 'categories' must be list-like"
with pytest.raises(TypeError, match=msg):
    CategoricalDtype("category")
