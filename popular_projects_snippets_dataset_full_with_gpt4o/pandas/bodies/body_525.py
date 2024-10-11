# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "Categorical categories must be unique"
with pytest.raises(ValueError, match=msg):
    CategoricalDtype([1, 2, 1])
