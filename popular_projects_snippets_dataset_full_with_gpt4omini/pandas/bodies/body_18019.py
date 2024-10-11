# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args_and_kwargs.py
bad_arg = "bar"
min_fname_arg_count = 2

compat_args = {"foo": -5, bad_arg: 1}

msg = (
    rf"the '{bad_arg}' parameter is not supported "
    rf"in the pandas implementation of {_fname}\(\)"
)

with pytest.raises(ValueError, match=msg):
    validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
