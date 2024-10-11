# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args_and_kwargs.py
compat_args = ("foo", "bar", "baz")
kwargs = {"foo": "FOO", "bar": "BAR"}
args = ("FoO", "BaZ")

min_fname_arg_count = 2
max_length = len(compat_args) + min_fname_arg_count
actual_length = len(kwargs) + len(args) + min_fname_arg_count

msg = (
    rf"{_fname}\(\) takes at most {max_length} "
    rf"arguments \({actual_length} given\)"
)

with pytest.raises(TypeError, match=msg):
    validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
