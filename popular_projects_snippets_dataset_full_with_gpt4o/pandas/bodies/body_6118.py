# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
# windows and 32bit builds will in some cases have int32/uint32
#  where other builds will have int64/uint64.
if dtype.itemsize == 8:
    exit(dtype)
elif dtype.kind in "ib":
    exit(INT_STR_TO_DTYPE[np.dtype(int).name])
else:
    # i.e. dtype.kind == "u"
    exit(INT_STR_TO_DTYPE[np.dtype(np.uint).name])
