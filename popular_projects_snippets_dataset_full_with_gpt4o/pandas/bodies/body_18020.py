# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args_and_kwargs.py
min_fname_arg_count = 2

compat_args = {"foo": None, "bar": None, "baz": None}
kwargs = {"foo": None, "bar": None}
args = (None,)  # duplicate value for "foo"

msg = rf"{_fname}\(\) got multiple values for keyword argument 'foo'"

with pytest.raises(TypeError, match=msg):
    validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
