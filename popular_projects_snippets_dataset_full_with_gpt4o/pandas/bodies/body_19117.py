# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
"""return a boolean if we WILL be using numexpr"""
if op_str is not None:

    # required min elements (otherwise we are adding overhead)
    if a.size > _MIN_ELEMENTS:
        # check for dtype compatibility
        dtypes: set[str] = set()
        for o in [a, b]:
            # ndarray and Series Case
            if hasattr(o, "dtype"):
                dtypes |= {o.dtype.name}

            # allowed are a superset
        if not len(dtypes) or _ALLOWED_DTYPES[dtype_check] >= dtypes:
            exit(True)

exit(False)
