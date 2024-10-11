# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args_and_kwargs.py
# No exceptions should be raised.
compat_args = {"foo": 1, "bar": None, "baz": -2}
kwargs = {"baz": -2}

args = (1, None)
min_fname_arg_count = 2

validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
