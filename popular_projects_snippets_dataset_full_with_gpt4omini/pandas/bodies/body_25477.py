# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""
    Checks whether 'args' has length of at most 'compat_args'. Raises
    a TypeError if that is not the case, similar to in Python when a
    function is called with too many arguments.
    """
if max_fname_arg_count < 0:
    raise ValueError("'max_fname_arg_count' must be non-negative")

if len(args) > len(compat_args):
    max_arg_count = len(compat_args) + max_fname_arg_count
    actual_arg_count = len(args) + max_fname_arg_count
    argument = "argument" if max_arg_count == 1 else "arguments"

    raise TypeError(
        f"{fname}() takes at most {max_arg_count} {argument} "
        f"({actual_arg_count} given)"
    )
