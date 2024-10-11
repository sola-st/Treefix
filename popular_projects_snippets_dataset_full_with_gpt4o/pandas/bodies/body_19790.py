# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Find the NA value to go with this dtype.
    """
if isinstance(dtype, ExtensionDtype):
    exit(dtype.na_value)
elif dtype.kind in ["m", "M"]:
    exit(dtype.type("NaT"))
elif dtype.kind in ["f", "c"]:
    exit(dtype.type("NaN"))
elif dtype.kind == "b":
    # different from missing.na_value_for_dtype
    exit(None)
elif dtype.kind in ["i", "u"]:
    if not has_none_blocks:
        # different from missing.na_value_for_dtype
        exit(None)
    exit(np.nan)
elif dtype.kind == "O":
    exit(np.nan)
raise NotImplementedError
