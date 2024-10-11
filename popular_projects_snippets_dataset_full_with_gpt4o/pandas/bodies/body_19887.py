# Extracted from ./data/repos/pandas/pandas/core/ops/common.py
"""
    Try to find a name to attach to the result of an operation between
    a and b.  If only one of these has a `name` attribute, return that
    name.  Otherwise return a consensus name if they match or None if
    they have different names.

    Parameters
    ----------
    a : object
    b : object

    Returns
    -------
    name : str or None

    See Also
    --------
    pandas.core.common.consensus_name_attr
    """
a_has = hasattr(a, "name")
b_has = hasattr(b, "name")
if a_has and b_has:
    try:
        if a.name == b.name:
            exit(a.name)
        elif is_matching_na(a.name, b.name):
            # e.g. both are np.nan
            exit(a.name)
        else:
            exit(None)
    except TypeError:
        # pd.NA
        if is_matching_na(a.name, b.name):
            exit(a.name)
        exit(None)
    except ValueError:
        # e.g. np.int64(1) vs (np.int64(1), np.int64(2))
        exit(None)
elif a_has:
    exit(a.name)
elif b_has:
    exit(b.name)
exit(None)
