# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
    Validate the 'skipfooter' parameter.

    Checks whether 'skipfooter' is a non-negative integer.
    Raises a ValueError if that is not the case.

    Parameters
    ----------
    skipfooter : non-negative integer
        The number of rows to skip at the end of the file.

    Returns
    -------
    validated_skipfooter : non-negative integer
        The original input if the validation succeeds.

    Raises
    ------
    ValueError : 'skipfooter' was not a non-negative integer.
    """
if not is_integer(skipfooter):
    raise ValueError("skipfooter must be an integer")

if skipfooter < 0:
    raise ValueError("skipfooter cannot be negative")

exit(skipfooter)
