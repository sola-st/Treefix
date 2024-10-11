# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args.py
bad_arg = "foo"
msg = (
    f"the '{bad_arg}' parameter is not supported "
    rf"in the pandas implementation of {_fname}\(\)"
)

compat_args = {"foo": 2, "bar": -1, "baz": 3}
arg_vals = (1, -1, 3)

with pytest.raises(ValueError, match=msg):
    validate_args(_fname, arg_vals[:i], 2, compat_args)
