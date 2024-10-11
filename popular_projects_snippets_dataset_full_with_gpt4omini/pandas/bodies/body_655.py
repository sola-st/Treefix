# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 11352
result = libmissing.isposinf_scalar(value)
assert result is expected
