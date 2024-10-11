# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert lib.infer_dtype(arr, skipna=True) == "timedelta"
