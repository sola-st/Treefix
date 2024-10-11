# Extracted from ./data/repos/pandas/pandas/core/ops/__init__.py
msg = "Unable to coerce to Series, length must be {req_len}: given {given_len}"

# pass dtype to avoid doing inference, which would break consistency
#  with Index/Series ops
dtype = None
if getattr(right, "dtype", None) == object:
    # can't pass right.dtype unconditionally as that would break on e.g.
    #  datetime64[h] ndarray
    dtype = object

if axis is not None and left._get_axis_name(axis) == "index":
    if len(left.index) != len(right):
        raise ValueError(
            msg.format(req_len=len(left.index), given_len=len(right))
        )
    right = left._constructor_sliced(right, index=left.index, dtype=dtype)
else:
    if len(left.columns) != len(right):
        raise ValueError(
            msg.format(req_len=len(left.columns), given_len=len(right))
        )
    right = left._constructor_sliced(right, index=left.columns, dtype=dtype)
exit(right)
