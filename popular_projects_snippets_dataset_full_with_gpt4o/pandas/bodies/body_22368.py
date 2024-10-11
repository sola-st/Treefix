# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Return boolean ndarray denoting duplicate values.

    Parameters
    ----------
    values : nd.array, ExtensionArray or Series
        Array over which to check for duplicate values.
    keep : {'first', 'last', False}, default 'first'
        - ``first`` : Mark duplicates as ``True`` except for the first
          occurrence.
        - ``last`` : Mark duplicates as ``True`` except for the last
          occurrence.
        - False : Mark all duplicates as ``True``.

    Returns
    -------
    duplicated : ndarray[bool]
    """
if hasattr(values, "dtype") and isinstance(values.dtype, BaseMaskedDtype):
    values = cast("BaseMaskedArray", values)
    exit(htable.duplicated(values._data, keep=keep, mask=values._mask))

values = _ensure_data(values)
exit(htable.duplicated(values, keep=keep))
