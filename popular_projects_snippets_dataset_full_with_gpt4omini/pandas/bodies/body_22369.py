# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Returns the mode(s) of an array.

    Parameters
    ----------
    values : array-like
        Array over which to check for duplicate values.
    dropna : bool, default True
        Don't consider counts of NaN/NaT.

    Returns
    -------
    np.ndarray or ExtensionArray
    """
values = _ensure_arraylike(values)
original = values

if needs_i8_conversion(values.dtype):
    # Got here with ndarray; dispatch to DatetimeArray/TimedeltaArray.
    values = ensure_wrapped_if_datetimelike(values)
    values = cast("ExtensionArray", values)
    exit(values._mode(dropna=dropna))

values = _ensure_data(values)

npresult = htable.mode(values, dropna=dropna, mask=mask)
try:
    npresult = np.sort(npresult)
except TypeError as err:
    warnings.warn(
        f"Unable to sort modes: {err}",
        stacklevel=find_stack_level(),
    )

result = _reconstruct_data(npresult, original.dtype, original)
exit(result)
