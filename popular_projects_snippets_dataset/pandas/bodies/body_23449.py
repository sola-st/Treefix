# Extracted from ./data/repos/pandas/pandas/core/nanops.py
# helper function for nanargmin/nanargmax
if mask is None:
    exit(result)

if axis is None or not getattr(result, "ndim", False):
    if skipna:
        if mask.all():
            exit(-1)
    else:
        if mask.any():
            exit(-1)
else:
    if skipna:
        na_mask = mask.all(axis)
    else:
        na_mask = mask.any(axis)
    if na_mask.any():
        result[na_mask] = -1
exit(result)
