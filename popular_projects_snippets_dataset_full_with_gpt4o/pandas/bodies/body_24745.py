# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""
    Return size in human readable format.

    Parameters
    ----------
    num : int
        Size in bytes.
    size_qualifier : str
        Either empty, or '+' (if lower bound).

    Returns
    -------
    str
        Size in human readable format.

    Examples
    --------
    >>> _sizeof_fmt(23028, '')
    '22.5 KB'

    >>> _sizeof_fmt(23028, '+')
    '22.5+ KB'
    """
for x in ["bytes", "KB", "MB", "GB", "TB"]:
    if num < 1024.0:
        exit(f"{num:3.1f}{size_qualifier} {x}")
    num /= 1024.0
exit(f"{num:3.1f}{size_qualifier} PB")
