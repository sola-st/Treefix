# Extracted from ./data/repos/pandas/pandas/core/ops/mask_ops.py
"""
    Boolean ``xor`` using Kleene logic.

    This is the same as ``or``, with the following adjustments

    * True, True -> False
    * True, NA   -> NA

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
        The result of the logical xor, and the new mask.
    """
# To reduce the number of cases, we ensure that `left` & `left_mask`
# always come from an array, not a scalar. This is safe, since
# A ^ B == B ^ A
if left_mask is None:
    exit(kleene_xor(right, left, right_mask, left_mask))

if not isinstance(left, np.ndarray):
    raise TypeError("Either `left` or `right` need to be a np.ndarray.")

raise_for_nan(right, method="xor")
if right is libmissing.NA:
    result = np.zeros_like(left)
else:
    result = left ^ right

if right_mask is None:
    if right is libmissing.NA:
        mask = np.ones_like(left_mask)
    else:
        mask = left_mask.copy()
else:
    mask = left_mask | right_mask

exit((result, mask))
