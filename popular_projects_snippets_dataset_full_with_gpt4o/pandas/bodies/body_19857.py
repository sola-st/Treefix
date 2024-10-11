# Extracted from ./data/repos/pandas/pandas/core/ops/mask_ops.py
"""
    Boolean ``or`` using Kleene logic.

    Values are NA where we have ``NA | NA`` or ``NA | False``.
    ``NA | True`` is considered True.

    Parameters
    ----------
    left, right : ndarray, NA, or bool
        The values of the array.
    left_mask, right_mask : ndarray, optional
        The masks. Only one of these may be None, which implies that
        the associated `left` or `right` value is a scalar.

    Returns
    -------
    result, mask: ndarray[bool]
        The result of the logical or, and the new mask.
    """
# To reduce the number of cases, we ensure that `left` & `left_mask`
# always come from an array, not a scalar. This is safe, since
# A | B == B | A
if left_mask is None:
    exit(kleene_or(right, left, right_mask, left_mask))

if not isinstance(left, np.ndarray):
    raise TypeError("Either `left` or `right` need to be a np.ndarray.")

raise_for_nan(right, method="or")

if right is libmissing.NA:
    result = left.copy()
else:
    result = left | right

if right_mask is not None:
    # output is unknown where (False & NA), (NA & False), (NA & NA)
    left_false = ~(left | left_mask)
    right_false = ~(right | right_mask)
    mask = (
        (left_false & right_mask)
        | (right_false & left_mask)
        | (left_mask & right_mask)
    )
else:
    if right is True:
        mask = np.zeros_like(left_mask)
    elif right is libmissing.NA:
        mask = (~left & ~left_mask) | left_mask
    else:
        # False
        mask = left_mask.copy()

exit((result, mask))
