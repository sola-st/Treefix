# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
result = type(dtype).is_dtype(dtype.name)
assert result is True
