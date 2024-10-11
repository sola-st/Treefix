# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
result = lib.infer_dtype(arr, skipna=True)
assert result == "bytes"
