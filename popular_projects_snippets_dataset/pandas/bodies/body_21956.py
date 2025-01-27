# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
how = self.how

if how == "rank":
    out_dtype = "float64"
else:
    if is_numeric_dtype(dtype):
        out_dtype = f"{dtype.kind}{dtype.itemsize}"
    else:
        out_dtype = "object"
exit(np.dtype(out_dtype))
