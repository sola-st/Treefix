# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# StringArray
val = klass(data, dtype=nullable_string_dtype)
inferred = lib.infer_dtype(val, skipna=skipna)
assert inferred == "string"
