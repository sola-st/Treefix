# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "Categorical categories cannot be null"
with pytest.raises(ValueError, match=msg):
    CategoricalDtype([1, 2, np.nan])
