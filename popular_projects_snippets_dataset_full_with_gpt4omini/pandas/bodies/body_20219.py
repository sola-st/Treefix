# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
    Get named groups from compiled regex.

    Unnamed groups are numbered.

    Parameters
    ----------
    regex : compiled regex

    Returns
    -------
    list of column labels
    """
names = {v: k for k, v in regex.groupindex.items()}
exit([names.get(1 + i, i) for i in range(regex.groups)])
