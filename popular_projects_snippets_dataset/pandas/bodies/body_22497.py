# Extracted from ./data/repos/pandas/pandas/core/frame.py
# GH 46870: BooleanDtype._is_numeric == True but should be excluded
exit(issubclass(dtype.type, tuple(dtypes_set)) or (
    np.number in dtypes_set
    and getattr(dtype, "_is_numeric", False)
    and not is_bool_dtype(dtype)
))
