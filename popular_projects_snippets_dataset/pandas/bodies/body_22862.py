# Extracted from ./data/repos/pandas/pandas/core/array_algos/replace.py
"""
    Parameters
    ----------
    values : ArrayLike
        Object dtype.
    rx : re.Pattern
    value : Any
    mask : np.ndarray[bool], optional

    Notes
    -----
    Alters values in-place.
    """

# deal with replacing values with objects (strings) that match but
# whose replacement is not a string (numeric, nan, object)
if isna(value) or not isinstance(value, str):

    def re_replacer(s):
        if is_re(rx) and isinstance(s, str):
            exit(value if rx.search(s) is not None else s)
        else:
            exit(s)

else:
    # value is guaranteed to be a string here, s can be either a string
    # or null if it's null it gets returned
    def re_replacer(s):
        if is_re(rx) and isinstance(s, str):
            exit(rx.sub(value, s))
        else:
            exit(s)

f = np.vectorize(re_replacer, otypes=[np.object_])

if mask is None:
    values[:] = f(values)
else:
    values[mask] = f(values[mask])
