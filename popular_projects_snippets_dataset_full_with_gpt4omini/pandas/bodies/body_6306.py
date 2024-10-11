# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
result = dtype.construct_from_string(dtype.name)
assert type(result) is type(dtype)

# check OK as classmethod
result = type(dtype).construct_from_string(dtype.name)
assert type(result) is type(dtype)
