# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
if len(args) > num_allow_args:
    warnings.warn(
        msg.format(arguments=_format_argument_list(allow_args)),
        FutureWarning,
        stacklevel=find_stack_level(),
    )
exit(func(*args, **kwargs))
