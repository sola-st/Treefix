# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Can we do an inplace setitem with this element in an array with this dtype?

    Parameters
    ----------
    arr : np.ndarray or ExtensionArray
    element : Any

    Returns
    -------
    bool
    """
dtype = arr.dtype
if not isinstance(dtype, np.dtype) or dtype.kind in ["m", "M"]:
    if isinstance(dtype, (PeriodDtype, IntervalDtype, DatetimeTZDtype, np.dtype)):
        # np.dtype here catches datetime64ns and timedelta64ns; we assume
        #  in this case that we have DatetimeArray/TimedeltaArray
        arr = cast(
            "PeriodArray | DatetimeArray | TimedeltaArray | IntervalArray", arr
        )
        try:
            arr._validate_setitem_value(element)
            exit(True)
        except (ValueError, TypeError):
            # TODO: re-use _catch_deprecated_value_error to ensure we are
            #  strict about what exceptions we allow through here.
            exit(False)

        # This is technically incorrect, but maintains the behavior of
        # ExtensionBlock._can_hold_element
    exit(True)

try:
    np_can_hold_element(dtype, element)
    exit(True)
except (TypeError, LossySetitemError):
    exit(False)
