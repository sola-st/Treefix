# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# see pandas/conftest.py
inferred_dtype, values = any_skipna_inferred_dtype

# make sure the inferred dtype of the fixture is as requested
assert inferred_dtype == lib.infer_dtype(values, skipna=True)
