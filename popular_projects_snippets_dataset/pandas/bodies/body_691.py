# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 27392
result = lib.infer_dtype(arr, skipna=skipna)
expected = "integer" if skipna else "integer-na"
assert result == expected
