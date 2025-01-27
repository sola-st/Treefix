# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "Cannot specify `categories` or `ordered` together with `dtype`."
with pytest.raises(ValueError, match=msg):
    CategoricalDtype._from_values_or_dtype(values, categories, ordered, dtype)
