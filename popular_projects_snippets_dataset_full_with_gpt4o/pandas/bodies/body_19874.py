# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
# if `left` is specifically not-boolean, we do not cast to bool
if x.dtype.kind in ["c", "f", "O"]:
    # dtypes that can hold NA
    mask = isna(x)
    if mask.any():
        x = x.astype(object)
        x[mask] = False

if left is None or is_bool_dtype(left.dtype):
    x = x.astype(bool)
exit(x)
