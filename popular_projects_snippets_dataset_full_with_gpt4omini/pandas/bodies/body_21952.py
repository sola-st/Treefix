# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py

dtype_str = dtype.name
ftype = cls._CYTHON_FUNCTIONS[kind][how]

# see if there is a fused-type version of function
# only valid for numeric
f = getattr(libgroupby, ftype)
if is_numeric:
    exit(f)
elif dtype == np.dtype(object):
    if how in ["median", "cumprod"]:
        # no fused types -> no __signatures__
        raise NotImplementedError(
            f"function is not implemented for this dtype: "
            f"[how->{how},dtype->{dtype_str}]"
        )
    if "object" not in f.__signatures__:
        # raise NotImplementedError here rather than TypeError later
        raise NotImplementedError(
            f"function is not implemented for this dtype: "
            f"[how->{how},dtype->{dtype_str}]"
        )
    exit(f)
else:
    raise NotImplementedError(
        "This should not be reached. Please report a bug at "
        "github.com/pandas-dev/pandas/",
        dtype,
    )
