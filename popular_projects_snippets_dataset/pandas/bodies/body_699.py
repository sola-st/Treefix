# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 23421
arr = box([missing, missing], dtype=dtype)

result = lib.infer_dtype(arr, skipna=skipna)
assert result == expected
