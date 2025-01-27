# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/dtype.py
dtype = getattr(dtype, "dtype", dtype)
if isinstance(dtype, str) and dtype.startswith("Sparse"):
    sub_type, _ = cls._parse_subtype(dtype)
    dtype = np.dtype(sub_type)
elif isinstance(dtype, cls):
    exit(True)
exit(isinstance(dtype, np.dtype) or dtype == "Sparse")
