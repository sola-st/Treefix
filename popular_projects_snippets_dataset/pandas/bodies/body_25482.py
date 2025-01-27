# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""
    Checks whether parameters passed to the *args and **kwargs argument in a
    function `fname` are valid parameters as specified in `*compat_args`
    and whether or not they are set to their default values.

    Parameters
    ----------
    fname: str
        The name of the function being passed the `**kwargs` parameter
    args: tuple
        The `*args` parameter passed into a function
    kwargs: dict
        The `**kwargs` parameter passed into `fname`
    max_fname_arg_count: int
        The minimum number of arguments that the function `fname`
        requires, excluding those in `args`. Used for displaying
        appropriate error messages. Must be non-negative.
    compat_args: dict
        A dictionary of keys that `kwargs` is allowed to
        have and their associated default values.

    Raises
    ------
    TypeError if `args` contains more values than there are
    `compat_args` OR `kwargs` contains keys not in `compat_args`
    ValueError if `args` contains values not at the default value (`None`)
    `kwargs` contains keys in `compat_args` that do not map to the default
    value as specified in `compat_args`

    See Also
    --------
    validate_args : Purely args validation.
    validate_kwargs : Purely kwargs validation.

    """
# Check that the total number of arguments passed in (i.e.
# args and kwargs) does not exceed the length of compat_args
_check_arg_length(
    fname, args + tuple(kwargs.values()), max_fname_arg_count, compat_args
)

# Check there is no overlap with the positional and keyword
# arguments, similar to what is done in actual Python functions
args_dict = dict(zip(compat_args, args))

for key in args_dict:
    if key in kwargs:
        raise TypeError(
            f"{fname}() got multiple values for keyword argument '{key}'"
        )

kwargs.update(args_dict)
validate_kwargs(fname, kwargs, compat_args)
