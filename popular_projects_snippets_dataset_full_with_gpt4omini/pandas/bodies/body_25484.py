# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""
    Argument handler for mixed index, columns / axis functions

    In an attempt to handle both `.method(index, columns)`, and
    `.method(arg, axis=.)`, we have to do some bad things to argument
    parsing. This translates all arguments to `{index=., columns=.}` style.

    Parameters
    ----------
    data : DataFrame
    args : tuple
        All positional arguments from the user
    kwargs : dict
        All keyword arguments from the user
    arg_name, method_name : str
        Used for better error messages

    Returns
    -------
    kwargs : dict
        A dictionary of keyword arguments. Doesn't modify ``kwargs``
        inplace, so update them with the return value here.

    Examples
    --------
    >>> df = pd.DataFrame(range(2))
    >>> validate_axis_style_args(df, (str.upper,), {'columns': id},
    ...                          'mapper', 'rename')
    {'columns': <built-in function id>, 'index': <method 'upper' of 'str' objects>}
    """
# TODO: Change to keyword-only args and remove all this

out = {}
# Goal: fill 'out' with index/columns-style arguments
# like out = {'index': foo, 'columns': bar}

# Start by validating for consistency
if "axis" in kwargs and any(x in kwargs for x in data._AXIS_TO_AXIS_NUMBER):
    msg = "Cannot specify both 'axis' and any of 'index' or 'columns'."
    raise TypeError(msg)

# First fill with explicit values provided by the user...
if arg_name in kwargs:
    if args:
        msg = f"{method_name} got multiple values for argument '{arg_name}'"
        raise TypeError(msg)

    axis = data._get_axis_name(kwargs.get("axis", 0))
    out[axis] = kwargs[arg_name]

# More user-provided arguments, now from kwargs
for k, v in kwargs.items():
    try:
        ax = data._get_axis_name(k)
    except ValueError:
        pass
    else:
        out[ax] = v

    # All user-provided kwargs have been handled now.
    # Now we supplement with positional arguments, emitting warnings
    # when there's ambiguity and raising when there's conflicts

if len(args) == 0:
    pass  # It's up to the function to decide if this is valid
elif len(args) == 1:
    axis = data._get_axis_name(kwargs.get("axis", 0))
    out[axis] = args[0]
elif len(args) == 2:
    if "axis" in kwargs:
        # Unambiguously wrong
        msg = "Cannot specify both 'axis' and any of 'index' or 'columns'"
        raise TypeError(msg)

    msg = (
        f"'.{method_name}(a, b)' is ambiguous. Use named keyword arguments"
        "for 'index' or 'columns'."
    )
    raise TypeError(msg)
else:
    msg = f"Cannot specify all of '{arg_name}', 'index', 'columns'."
    raise TypeError(msg)
exit(out)
