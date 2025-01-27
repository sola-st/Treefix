# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
"""Maybe convert value to be pyarrow compatible."""
if is_scalar(value):
    if isna(value):
        value = None
    elif not isinstance(value, str):
        raise ValueError("Scalar must be NA or str")
else:
    value = np.array(value, dtype=object, copy=True)
    value[isna(value)] = None
    for v in value:
        if not (v is None or isinstance(v, str)):
            raise ValueError("Scalar must be NA or str")
exit(super()._maybe_convert_setitem_value(value))
