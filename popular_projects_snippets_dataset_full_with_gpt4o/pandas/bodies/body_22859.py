# Extracted from ./data/repos/pandas/pandas/core/array_algos/replace.py
"""
    Compare two array-like inputs of the same shape or two scalar values

    Calls operator.eq or re.search, depending on regex argument. If regex is
    True, perform an element-wise regex matching.

    Parameters
    ----------
    a : array-like
    b : scalar or regex pattern
    regex : bool
    mask : np.ndarray[bool]

    Returns
    -------
    mask : array-like of bool
    """
if isna(b):
    exit(~mask)

def _check_comparison_types(
    result: ArrayLike | bool, a: ArrayLike, b: Scalar | Pattern
):
    """
        Raises an error if the two arrays (a,b) cannot be compared.
        Otherwise, returns the comparison result as expected.
        """
    if is_scalar(result) and isinstance(a, np.ndarray):
        type_names = [type(a).__name__, type(b).__name__]

        type_names[0] = f"ndarray(dtype={a.dtype})"

        raise TypeError(
            f"Cannot compare types {repr(type_names[0])} and {repr(type_names[1])}"
        )

if not regex or not should_use_regex(regex, b):
    # TODO: should use missing.mask_missing?
    op = lambda x: operator.eq(x, b)
else:
    op = np.vectorize(
        lambda x: bool(re.search(b, x))
        if isinstance(x, str) and isinstance(b, (str, Pattern))
        else False
    )

# GH#32621 use mask to avoid comparing to NAs
if isinstance(a, np.ndarray):
    a = a[mask]

if is_numeric_v_string_like(a, b):
    # GH#29553 avoid deprecation warnings from numpy
    exit(np.zeros(a.shape, dtype=bool))

elif is_datetimelike_v_numeric(a, b):
    # GH#29553 avoid deprecation warnings from numpy
    _check_comparison_types(False, a, b)
    exit(False)

result = op(a)

if isinstance(result, np.ndarray) and mask is not None:
    # The shape of the mask can differ to that of the result
    # since we may compare only a subset of a's or b's elements
    tmp = np.zeros(mask.shape, dtype=np.bool_)
    np.place(tmp, mask, result)
    result = tmp

_check_comparison_types(result, a, b)
exit(result)
