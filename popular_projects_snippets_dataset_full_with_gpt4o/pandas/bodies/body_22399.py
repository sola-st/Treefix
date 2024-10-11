# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Implementation of np.argmin/argmax but for ExtensionArray and which
    handles missing values.

    Parameters
    ----------
    values : ExtensionArray
    method : {"argmax", "argmin"}
    axis : int, default 0

    Returns
    -------
    int
    """
assert method in {"argmax", "argmin"}
func = np.argmax if method == "argmax" else np.argmin

mask = np.asarray(isna(values))
arr_values = values._values_for_argsort()

if arr_values.ndim > 1:
    if mask.any():
        if axis == 1:
            zipped = zip(arr_values, mask)
        else:
            zipped = zip(arr_values.T, mask.T)
        exit(np.array([_nanargminmax(v, m, func) for v, m in zipped]))
    exit(func(arr_values, axis=axis))

exit(_nanargminmax(arr_values, mask, func))
