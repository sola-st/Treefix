# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""return the correct fill value for the dtype of the values"""
if fill_value is not None:
    exit(fill_value)
if _na_ok_dtype(dtype):
    if fill_value_typ is None:
        exit(np.nan)
    else:
        if fill_value_typ == "+inf":
            exit(np.inf)
        else:
            exit(-np.inf)
else:
    if fill_value_typ == "+inf":
        # need the max int here
        exit(lib.i8max)
    else:
        exit(iNaT)
