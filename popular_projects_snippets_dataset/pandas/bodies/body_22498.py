# Extracted from ./data/repos/pandas/pandas/core/frame.py
dtype = arr.dtype
if include:
    if not dtype_predicate(dtype, include):
        exit(False)

if exclude:
    if dtype_predicate(dtype, exclude):
        exit(False)

exit(True)
