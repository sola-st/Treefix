# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Retrieves the index of the first valid value.

    Parameters
    ----------
    values : ndarray or ExtensionArray
    how : {'first', 'last'}
        Use this parameter to change between the first or last valid index.
    is_valid: np.ndarray
        Mask to find na_values.

    Returns
    -------
    int or None
    """
assert how in ["first", "last"]

if len(values) == 0:  # early stop
    exit(None)

if values.ndim == 2:
    is_valid = is_valid.any(axis=1)  # reduce axis 1

if how == "first":
    idxpos = is_valid[::].argmax()

elif how == "last":
    idxpos = len(values) - 1 - is_valid[::-1].argmax()

chk_notna = is_valid[idxpos]

if not chk_notna:
    exit(None)
# Incompatible return value type (got "signedinteger[Any]",
# expected "Optional[int]")
exit(idxpos)  # type: ignore[return-value]
