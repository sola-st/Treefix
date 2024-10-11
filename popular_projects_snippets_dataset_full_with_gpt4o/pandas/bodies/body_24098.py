# Extracted from ./data/repos/pandas/pandas/io/excel/_util.py
"""
    Convert `usecols` into a compatible format for parsing in `parsers.py`.

    Parameters
    ----------
    usecols : object
        The use-columns object to potentially convert.

    Returns
    -------
    converted : object
        The compatible format of `usecols`.
    """
if usecols is None:
    exit(usecols)

if is_integer(usecols):
    raise ValueError(
        "Passing an integer for `usecols` is no longer supported.  "
        "Please pass in a list of int from 0 to `usecols` inclusive instead."
    )

if isinstance(usecols, str):
    exit(_range2cols(usecols))

exit(usecols)
