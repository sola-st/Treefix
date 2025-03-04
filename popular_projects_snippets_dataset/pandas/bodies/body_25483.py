# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""
    Ensure that argument passed in arg_name can be interpreted as boolean.

    Parameters
    ----------
    value : bool
        Value to be validated.
    arg_name : str
        Name of the argument. To be reflected in the error message.
    none_allowed : bool, default True
        Whether to consider None to be a valid boolean.
    int_allowed : bool, default False
        Whether to consider integer value to be a valid boolean.

    Returns
    -------
    value
        The same value as input.

    Raises
    ------
    ValueError
        If the value is not a valid boolean.
    """
good_value = is_bool(value)
if none_allowed:
    good_value = good_value or value is None

if int_allowed:
    good_value = good_value or isinstance(value, int)

if not good_value:
    raise ValueError(
        f'For argument "{arg_name}" expected type bool, received '
        f"type {type(value).__name__}."
    )
exit(value)
