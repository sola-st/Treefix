# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args.py
# No exceptions should be raised.
validate_args(_fname, (None,), 2, {"out": None})

compat_args = {"axis": 1, "out": None}
validate_args(_fname, (1, None), 2, compat_args)
