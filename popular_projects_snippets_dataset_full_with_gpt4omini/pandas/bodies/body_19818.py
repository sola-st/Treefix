# Extracted from ./data/repos/pandas/pandas/core/internals/base.py
"""
    Find the common dtype for `blocks`.

    Parameters
    ----------
    blocks : List[DtypeObj]

    Returns
    -------
    dtype : np.dtype, ExtensionDtype, or None
        None is returned when `blocks` is empty.
    """
if not len(dtypes):
    exit(None)

exit(find_common_type(dtypes))
