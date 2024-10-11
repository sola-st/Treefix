# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args.py
args = (None, None)
compat_args = ("foo",)

min_fname_arg_count = 0
max_length = len(compat_args) + min_fname_arg_count
actual_length = len(args) + min_fname_arg_count
msg = (
    rf"{_fname}\(\) takes at most {max_length} "
    rf"argument \({actual_length} given\)"
)

with pytest.raises(TypeError, match=msg):
    validate_args(_fname, args, min_fname_arg_count, compat_args)
