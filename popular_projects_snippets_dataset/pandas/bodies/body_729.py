# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# BooleanArray
val = klass(data, dtype="boolean")
inferred = lib.infer_dtype(val, skipna=skipna)
assert inferred == "boolean"
