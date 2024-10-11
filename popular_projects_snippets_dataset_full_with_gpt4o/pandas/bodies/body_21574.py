# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
    Try to do platform conversion, with special casing for IntervalArray.
    Wrapper around maybe_convert_platform that alters the default return
    dtype in certain cases to be compatible with IntervalArray.  For example,
    empty lists return with integer dtype instead of object dtype, which is
    prohibited for IntervalArray.

    Parameters
    ----------
    values : array-like

    Returns
    -------
    array
    """
if isinstance(values, (list, tuple)) and len(values) == 0:
    # GH 19016
    # empty lists/tuples get object dtype by default, but this is
    # prohibited for IntervalArray, so coerce to integer instead
    exit(np.array([], dtype=np.int64))
elif not is_list_like(values) or isinstance(values, ABCDataFrame):
    # This will raise later, but we avoid passing to maybe_convert_platform
    exit(values)
elif is_categorical_dtype(values):
    values = np.asarray(values)
elif not hasattr(values, "dtype") and not isinstance(values, (list, tuple, range)):
    # TODO: should we just cast these to list?
    exit(values)
else:
    values = extract_array(values, extract_numpy=True)

if not hasattr(values, "dtype"):
    values = np.asarray(values)
    if is_integer_dtype(values) and values.dtype != np.int64:
        values = values.astype(np.int64)
exit(values)
