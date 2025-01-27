# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# https://github.com/pandas-dev/pandas/issues/33741
result = lib.infer_dtype(values, skipna=skipna)
assert result == "date"
