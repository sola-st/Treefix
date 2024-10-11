# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_kwargs.py
# No exceptions should be raised.
compat_args = {"f": None, "b": 1, "ba": "s"}

kwargs = {"f": None, "b": 1}
validate_kwargs(_fname, kwargs, compat_args)
