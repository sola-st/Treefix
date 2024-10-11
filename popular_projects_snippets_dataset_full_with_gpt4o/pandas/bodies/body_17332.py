# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
cls, init_args, method = ndframe_method
ndframe = cls(*init_args)

ndframe.attrs = {"a": 1}
result = method(ndframe)

assert result.attrs == {"a": 1}
