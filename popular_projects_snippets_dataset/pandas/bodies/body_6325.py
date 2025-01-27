# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
# only testing that this works without raising an error
res = infer_dtype(data, skipna=skipna)
assert isinstance(res, str)
res = infer_dtype(data_missing, skipna=skipna)
assert isinstance(res, str)
