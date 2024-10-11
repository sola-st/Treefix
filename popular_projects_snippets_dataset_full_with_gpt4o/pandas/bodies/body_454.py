# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "Cannot not construct CategoricalDtype from <class 'object'>"
with pytest.raises(ValueError, match=msg):
    CategoricalDtype._from_values_or_dtype(None, None, None, object)
